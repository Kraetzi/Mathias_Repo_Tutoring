class Obstacle {

    void print(String name) {
        System.out.println(name);
    }

    void print(String name, int age) {
        System.out.println(name + '  ' + String(age));
    }

    void print(String name, int age, String address) {
         System.out.println(name + '  ' + String(age) + ' ' + address);
    } 


}

Obstacle o1 = new Obstacle();
o1.print("Mathias", 40);