package com.example.dell.student_manger;

import android.content.Context;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

public class MyDatabaseHelper extends SQLiteOpenHelper {
    public static final String CREATE_S_T = "create table student_message(" //建表语句
            + "name text,"
            + "id text PRIMARY KEY,"
            + "age text)";
    public MyDatabaseHelper(Context context,String name,SQLiteDatabase.CursorFactory factory, int version){
        super(context,name,factory,version);

    }
    @Override
    public void onCreate(SQLiteDatabase db){
        db.execSQL(CREATE_S_T);
    }
    @Override
    public void onUpgrade(SQLiteDatabase db,int oldVersion,int newVersion){}

}
