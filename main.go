package main

import (
	"fmt"
	"log"
	"read/constants"
	"strconv"

	"github.com/xuri/excelize/v2"
)

func main() {
	archivoPrincipal := "G:\\ReadWriteFile\\ReadWriteFile\\template\\FORMATO-COVID.xlsx"
	f, err := excelize.OpenFile(archivoPrincipal) 	// Abrir el archivo principal
	if err != nil {
		log.Fatal(err)
	}

	hojaTriage := constants.Triage
	hojaOdontologia := constants.RegOdontologia

	// Solicitar el ID por consola
	fmt.Print("Ingrese el ID a buscar: ")
	var id string
	if _, err = fmt.Scanln(&id); err != nil {
		log.Fatal(err)
	}

	// Buscar el ID en la columna I de TRIAGE
	hojaTriageData, _ := f.GetRows(hojaTriage)
	filaEncontrada := -1

	for i, fila := range hojaTriageData {
		if len(fila) >= 9 && fila[8] == id {
			filaEncontrada = i
			break
		}
	}

	if filaEncontrada == -1 {
		fmt.Println("No se encontró el ID en la hoja TRIAGE.")
		return
	}

	// Obtener la fila completa en TRIAGE
	filaTriage := hojaTriageData[filaEncontrada]

	// Obtener los datos de la hoja REG.ODONTOLOGIA
	hojaOdontologiaData, _ := f.GetRows(hojaOdontologia)

	// Obtener la siguiente fila disponible en REG.ODONTOLOGIA
	filaNueva := obtenerSiguienteFila(hojaOdontologiaData)

	// Copiar y pegar la fila completa en REG.ODONTOLOGIA
	hojaOdontologiaData = append(hojaOdontologiaData, filaTriage)
	copiarFilaCompleta(f, hojaOdontologia, filaTriage, filaNueva)

	// Guardar los cambios en el archivo
	if err = f.SaveAs(archivoPrincipal); err != nil {
		log.Fatal(err)
	}

	fmt.Println("La fila se ha copiado y pegado correctamente en la hoja REG.ODONTOLOGIA.")
}

func obtenerSiguienteFila(hojaOdontologiaData [][]string) int {
	numFilas := len(hojaOdontologiaData)
	if numFilas == 0 {
		return 1 // La hoja está vacía, la nueva fila será la primera (fila 1)
	}
	return numFilas + 1 // Utilizar la siguiente fila después de la última fila no vacía
}

func copiarFilaCompleta(f *excelize.File, hojaOdontologia string, fila []string, filaNueva int) {
	// Pegar la data desde la columna A
	indiceSinEspacios := 1 // Inicializamos el índice para la fila sin espacios en 1
	encontradoDato := false

	for i := 0; i < len(fila)-1; i++ {
		valor := fila[i]

		if valor != constants.EmptyString || encontradoDato {
			celda := indiceAColumna(indiceSinEspacios) + strconv.Itoa(filaNueva)
			f.SetCellValue(hojaOdontologia, celda, valor)
			indiceSinEspacios++
			encontradoDato = true
		}
	}
}

func indiceAColumna(indice int) string {
	letra := constants.EmptyString
	for indice > 0 {
		indice--
		letra = string('A'+indice%26) + letra
		indice = indice / 26
	}
	return letra
}
