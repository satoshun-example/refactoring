// Before
class Walk {
    private final double speedPerHour;
    private final double times;

    public Walk(double speedPerHour, double times) {
        this.speedPerHour = speedPerHour;
        this.times = times;
    }

    public double weekDayDistance() {
        double distance = speedPerHour * times;

        if (distance >= 10.0) {
            distance *= 0.9;
        }

        return distance * 5.0;
    }

    public String toString() {
        return getClass().getSimpleName();
    }
}

// After
class Walk2 {
    private final double speedPerHour;
    private final double times;

    public Walk2(double speedPerHour, double times) {
        this.speedPerHour = speedPerHour;
        this.times = times;
    }

    public double weekDayDistance() {
        return baseDistance() * distanceCompensation() * 5.0;
    }

    private double baseDistance() {
        return speedPerHour * times;
    }

    private double distanceCompensation() {
        if (baseDistance() >= 10.0) return 0.9;
        return 1.0;
    }

    public String toString() {
        return getClass().getSimpleName();
    }
}


class ReplaceTempWithQuery {
    public static void main(String[] args) {
        Walk w = new Walk(50.5, 3.5);
        System.out.println(w);
        System.out.println(w.weekDayDistance());

        Walk2 w2 = new Walk2(50.5, 3.5);
        System.out.println(w2);
        System.out.println(w2.weekDayDistance());
    }
}
