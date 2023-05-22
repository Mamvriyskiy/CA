package main

import (
	"fmt"
	"math"
	"gonum.org/v1/gonum/mat"
)

const (
	eps = 0.01
)

func outputResult(i int, result []float64) {
	fmt.Println("===================")
	fmt.Printf("x%d = %f\n", i + 1, result[0])
	fmt.Printf("y%d = %f\n", i + 1, result[1])
	fmt.Printf("z%d = %f\n", i + 1, result[2])
	fmt.Println()
}

func F(x, y, z float64) (float64, float64, float64) {
	a := x * x + y * y + z * z - 1
	b := 2 * x * x + y * y - 4 * z
	c := 3 * x * x - 4 * y + z * z

	return a, b, c
}

func W(x, y, z float64) []float64 {
	w := []float64{2, 2, 2, 4, 2, -4, 6, -4, 2}

	for i, _ := range w {
		if i == 5 || i == 7 {
			continue
		}

		if i % 3 == 0 {
			w[i] *= x
		} else if i % 3 == 1 {
			w[i] *= y
		} else {
			w[i] *= z
		}
	}

	return w
}

func Newton() {
	x := []float64{0.5, 0.5, 0.5}
	lastX := make([]float64, 3, 3)

	// math.Abs(x - lastX) < eps
	for  i := 0; math.Abs(x[0] - lastX[0]) > eps; i++{
		//f(x)
		Fvalues := make([]float64, 3, 3)
		Fvalues[0], Fvalues[1], Fvalues[2] = F(x[0], x[1], x[2])

		//Подставили приближение после производной W(x)
		Wmatrix := W(x[0], x[1], x[2])

		// fmt.Println(Fvalues ,Wmatrix)

		//Обратная матрица
		a := mat.NewDense(3, 3, Wmatrix)

		inv := mat.NewDense(3, 3, nil)

		err := inv.Inverse(a)
		if err != nil {
			fmt.Println("Обратная матрица не существует.")
			return
		}

		// fmt.Println(mat.Formatted(inv))

		//умножение матриц W(x) * f(x)
		b := mat.NewDense(3, 1, Fvalues)

		result := mat.NewDense(3, 1, nil)
		result.Mul(inv, b)

		// fmt.Println(mat.Formatted(result))

		//Вычитание матрицы из приближения
		X := mat.NewDense(3, 1, x)
		result.Sub(X, result)

		// fmt.Println(mat.Formatted(result))

		lastX = x
		x = result.RawMatrix().Data

		outputResult(i, x)
	}
}

func main() {
	fmt.Println("x^2 + y^2 + z^2 = 1")
	fmt.Println("2x^2 + y^2 - 4z = 0")
	fmt.Println("3x^2 - 4y + z^2 = 0")

	Newton()

}



