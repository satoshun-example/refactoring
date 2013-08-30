package sample.refactoring;

class Calculator {
    public int total(int a, int b, int c) {
        a += b;
        a += c;
        return a;
    }

    public int total_refactor(int a, int b, int c) {
        int total;
        total = a;
        total += b;
        total += c;
        return total;
    }
}


class RemoveAssignmentsToParameters {
    public static void main(String[] args) {
        Calculator calculator = new Calculator();

        assert calculator.total(20, -10, 100) == calculator.total_refactor(20, -10, 100);
    }
}
