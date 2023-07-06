package main

import (
	"fmt"
	"log"
	"os"
	"read/constants"
	"strconv"

	"github.com/xuri/excelize/v2"
)

func main() {
	if len(os.Args) < 3 {
		fmt.Println("Debe proporcionar el número y la ruta del archivo como argumentos.")
		return
	}

	numero, err := strconv.Atoi(os.Args[1])
	if err != nil {
		log.Fatal(err)
	}

	rutaExcel := os.Args[2]

	f, err := excelize.OpenFile(rutaExcel) // Abrir el archivo principal
	if err != nil {
		log.Fatal(err)
	}

	hojaTriage := constants.Triage
	hojaOdontologia := constants.RegOdontologia

	// Buscar el ID en la columna I de TRIAGE
	hojaTriageData, _ := f.GetRows(hojaTriage)
	filaEncontrada := -1

	for i, fila := range hojaTriageData {
		if len(fila) >= 9 && fila[8] == strconv.Itoa(numero) {
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
	if err = f.Save(); err != nil {
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
