package game;

public class Entity {
    String name;
    double hp;
    double atk;


    public Entity(String name, double hp, double atk) {
        this.name = name;
        this.hp = hp;
        this.atk = atk;
    }


    public String getName() {
        return name;

    }

    /**
     * sets Entity name
     * @param name
     */
    public void setName(String name) {
        this.name = name;
    }

    /**
     * hp getter
     * @return Entity hit points
     */
    public double getHp() {
        return hp;
    }

    public void setHp(double hp) {
        this.hp = hp;
    }



    public double getAtk() {
        return atk;
    }

    /**
     *
     * @param atk
     */
    public void setAtk(double atk) {
        this.atk = atk;
    }

    /**
     * deals specified number of damage points to Entity
     * @param damage the attackers attack stat
     */
    public void takeDamage(double damage) {
        this.hp -= damage;
    }

    /**
     *attacks enemy entity
     * @param victim Entity to attack
     */
    public void attack(Entity victim) {
        victim.takeDamage(this.atk);
    }
}
