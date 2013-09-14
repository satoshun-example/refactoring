package sample.refactoring;

// before

class Person {
    private String name;
    private int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public void incAge() {
        age += 1;
    }

    public void changeName(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }
}


// after

interface IProfile {
    String getName();
    int getAge();
}


class Person2 implements IProfile {
    private String name;
    private int age;

    public Person2(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public void incAge() {
        age += 1;
    }

    public void changeName(String name) {
        this.name = name;
    }

    @Override
    public String getName() {
        return name;
    }

    @Override
    public int getAge() {
        return age;
    }
}


class ExtractInterface {
    public static void main(String[] args) {
        Person person = new Person("Ken", 20);
        System.out.println(person.getAge() + " : " + person.getName());
        person.incAge();
        System.out.println(person.getAge() + " : " + person.getName());

        IProfile profile = new Person2("Ken", 20);
        System.out.println(profile.getAge() + " : " + profile.getName());
    }
}
