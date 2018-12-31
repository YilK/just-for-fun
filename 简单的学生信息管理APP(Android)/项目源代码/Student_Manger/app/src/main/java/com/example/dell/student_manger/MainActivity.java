package com.example.dell.student_manger;

import android.content.ContentValues;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;

import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity implements View.OnClickListener {

    private MyDatabaseHelper dbHelper;
    private List<Student> studentList = new ArrayList<>();
    private EditText text_name;
    private EditText text_id;
    private EditText text_age;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main); //加载布局

        dbHelper = new MyDatabaseHelper(this, "Student_message3.db", null, 1);

        Button add_Button = (Button) findViewById(R.id.add);  //添加按钮
        Button delete_Button = (Button) findViewById(R.id.delete);  //删除按钮
        Button update_Button = (Button) findViewById(R.id.update);  //更新按钮
        Button select_Button = (Button) findViewById(R.id.select);  //查询按钮

                initStudents();//加载数据库中的数据
        StudentAdapter adapter = new StudentAdapter(MainActivity.this, R.layout.student_item, studentList);
        //R.layout.student_item 为子布局的id,studentList 存储着数据库中的数据
        ListView listView = (ListView) findViewById(R.id.list_view);  //listView组件
        listView.setAdapter(adapter);

        text_name = (EditText) findViewById(R.id.name); //姓名编辑框
        text_id = (EditText) findViewById(R.id.ID);   //学号编辑框
        text_age = (EditText) findViewById(R.id.age); //年龄编辑框
        //点击按钮
        add_Button.setOnClickListener(this);
        delete_Button.setOnClickListener(this);
        update_Button.setOnClickListener(this);
        select_Button.setOnClickListener(this);

    }

    @Override
    public void onClick(View v) {
        switch (v.getId()) {
            case R.id.add:  //添加按钮被点击
                SQLiteDatabase db1 = dbHelper.getWritableDatabase();
                ContentValues values1 = new ContentValues();

                //添加数据
                values1.put("name", text_name.getText().toString());
                values1.put("id", text_id.getText().toString());
                values1.put("age", text_age.getText().toString());

                //插入数据到数据库中  table：表  第二个参数：当有些字段没有数据插入时插入可以为空的列插入null，
                // 第三个参数：ContentValues 对象
                db1.insert("student_message", null, values1);
                break;

            case R.id.delete://删除按钮被点击
                SQLiteDatabase db2 = dbHelper.getWritableDatabase();
                //id 是唯一的非空的 所以可以直接使用id值删除
                db2.delete("student_message", "id=?", new String[]{text_id.getText().toString()});
                break;

            case R.id.update://更新按钮被点击
                SQLiteDatabase db3 = dbHelper.getWritableDatabase();
                ContentValues values2 = new ContentValues();
                values2.put("name", text_name.getText().toString());
                values2.put("age", text_age.getText().toString());
                db3.update("student_message", values2, "id=?", new String[]{text_id.getText().toString()});
                break;
            case R.id.select://查询按钮被点击
                //分两种情况
                //1.按学号查询姓名和年龄
                //2.按姓名查询学号和年龄

                //1.
                if (text_name.getText().toString().equals("")){//如果编辑学号栏不为空（在学号栏输入学号进行查询
                    SQLiteDatabase db4 = dbHelper.getWritableDatabase();
                    Cursor cursor = db4.query("student_message", new String[]{"name","age"}, "id=?",
                        new String[]{text_id.getText().toString()}, null, null, null);
                    String name="null";//表示无对应结果
                    String age="null";
                    if (cursor.moveToFirst()){
                        do {
                            name = cursor.getString(cursor.getColumnIndex("name"));  //姓名
                            age = cursor.getString(cursor.getColumnIndex("age"));    //年龄
                        }while (cursor.moveToNext());//数据指针移向下一行
                    }
                    cursor.close();
                    text_name.setText(name);
                    text_age.setText(age);
                }

                //2.
                else{//如果姓名栏不为空
                    SQLiteDatabase db5 = dbHelper.getWritableDatabase();
                    Cursor cursor=db5.query("student_message",new String[]{"id","age"},"name=?",
                            new String[]{text_name.getText().toString()},null,null,null);                    String name="null";//表示无对应结果
                    String id="";
                    String age="";
                    if (cursor.moveToFirst()){
                        do {
                                id+=cursor.getString(cursor.getColumnIndex("id"))+"  ";
                                age+=cursor.getString(cursor.getColumnIndex("age"))+"  ";
                        }while (cursor.moveToNext());//数据指针移向下一行
                        cursor.close();
                        text_id.setText(id);
                        text_age.setText(age);
                    }
                    else
                    {
                        text_id.setText("null");
                        text_age.setText("null");
                    }


                }
                break;
            default:
                break;
        }
        studentList.clear();
        initStudents();//初始化学生数据
        StudentAdapter adapter = new StudentAdapter(MainActivity.this, R.layout.student_item, studentList);
        //R.layout.student_item 为子布局的id
        ListView listView = (ListView) findViewById(R.id.list_view);
        listView.setAdapter(adapter);//加载构造好的适配器对象加载进去
    }

    public void initStudents() {
        SQLiteDatabase db = dbHelper.getWritableDatabase(); //打开数据库

        //查找所有的数据
        Cursor cursor = db.query("student_message", null, null,
                null, null, null, null);
        if (cursor.moveToFirst()) {//将数据指针移到第一行的位置
            do {
                String name = cursor.getString(cursor.getColumnIndex("name"));  //姓名
                String id = cursor.getString(cursor.getColumnIndex("id"));  //学号
                String age = cursor.getString(cursor.getColumnIndex("age"));    //年龄

                Student student = new Student(name, id, age);
                studentList.add(student);//添加入studentList

            } while (cursor.moveToNext());//数据指针移向下一行
        }
        cursor.close();

    }
}
