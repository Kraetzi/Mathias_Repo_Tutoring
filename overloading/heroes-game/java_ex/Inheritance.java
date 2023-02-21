class Character {

    Character() {
        this.name = "Mathias"
    }

    void print() {
        System.out.println("this is the print from Character");
    }
}


class Monster extends Character {

    Monster() {
        
    }


    void print() {
        System.out.println("this is the print from Monster");
    }

}


class Hero extends Character {
    
    Hero() {

    }


    void print() {
        System.out.println("this is the print from Hero");
    }
}


List l = ArrayList<Character>;
Monster mosnter1 = Monster();
Hero hero1 = Hero();

Character hero1 = Hero();
hero1.print();

l.add(mosnter1);
l.add(hero1);