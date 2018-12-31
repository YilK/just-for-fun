package com.example.dell.student_manger;

public class Student {
    private String name;    //姓名
    private String ID;  //学号
    private String age; //年龄

    public Student(String name, String ID, String age) {
        this.name = name;
        this.ID = ID;
        this.age = age;
    }

    //返回姓名
    public String getName() {
        return name;
    }

    //返回学号
    public String getID() {
        return ID;
    }

    //返回年龄
    public String getAge() {
        return age;
    }


}
