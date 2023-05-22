package main

import (
	"fmt"
	"math"
)

//Функция плотности вероятности стандартного нормального распределения.
func f(x float64) float64 {
    return (1 / math.Sqrt(2 * math.Pi)) * math.Exp(-(x * x) / 2)
}

//Метод Симпсона
func simpson(xCur float64)  float64 {
	steps := 200 //количество шагов
	step := xCur / (float64(steps) * 2)

	//для хранения X
	xValues := make([]float64, steps * 2 + 1)
	for i := range xValues {
		xValues[i] = float64(i) * step
	}

	//для хранения f(x)
	funcValues := make([]float64, steps * 2 + 1)
	for i, el := range xValues {
		funcValues[i] = f(el)
	}

	//сумма всех значений f(x) на нечетных позициях массива funcValues.
	sumX1 := 0.0
	for i := 1; i < steps; i++ {
		sumX1 += funcValues[2 * i - 1]
	}

	//сумма всех четных позициях массива funcValues, за исключением первого и последнего
	sumX2 := 0.0
	for i := 1; i < steps - 1; i++ {
		sumX2 += funcValues[2 * i]
	}

	//Вычисляется результат интегрирования с помощью формулы метода Симпсона
	return (step / 3) * (funcValues[0] + funcValues[len(funcValues) - 1] + 4 * sumX1 + 2 * sumX2)
}

func main() {
	ans := simpson(0.78521)
	fmt.Println(ans)
}
