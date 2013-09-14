package sample.refactoring;

// Before

class Vehicle {
    protected int speed = 0;
    protected int distance = 0;

    public void move() {
        distance += speed;
    }

    public int getSpeed() {
        return speed;
    }
}

class Car extends Vehicle {
    private int count = 0;

    public void ride() {
        count += 1;
    }

    public void accerate(int value) {
        speed = speed + value / 2;
    }
}

class Bike extends Vehicle {
    public void accerate(int value) {
        speed += value;
    }

    public void horn() {
        System.out.println("Sound horn");
    }
}

// After

class Vehicle2 {
    protected int speed = 0;
    protected int distance = 0;

    public void move() {
        distance += speed;
    }

    /*
     * pull up accerate method
     */
    public void accerate(int value) {
        speed += value / getFriction();
    }

    public int getSpeed() {
        return speed;
    }

    protected int getFriction() {
        return 1;
    }
}


/*
 * pull up accerate method
 */
class Car2 extends Vehicle2 {
    private int count = 0;

    public void ride() {
        count += 1;
    }

    @Override
    protected int getFriction() {
        return 2;
    }
}


/*
 * pull up accerate method
 */
class Bike2 extends Vehicle2 {
    public void horn() {
        System.out.println("Sound horn");
    }
}


class PullUpMethod {
    public static void main(String[] args) {
        // Before
        Car car = new Car();
        car.accerate(100);
        System.out.println(car.getSpeed());

        Bike bike = new Bike();
        bike.accerate(100);
        System.out.println(bike.getSpeed());

        // After
        Vehicle2 vehicle = new Car2();
        vehicle.accerate(100);
        System.out.println(vehicle.getSpeed());

        vehicle = new Bike2();
        vehicle.accerate(100);
        System.out.println(vehicle.getSpeed());
    }
}
