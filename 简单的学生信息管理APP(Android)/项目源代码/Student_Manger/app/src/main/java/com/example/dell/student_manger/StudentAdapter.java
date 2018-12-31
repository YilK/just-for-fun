package com.example.dell.student_manger;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.TextView;

import java.util.List;

//自定义ListView适配器
public class StudentAdapter extends ArrayAdapter<Student>{
    private int resourceId;

    public StudentAdapter(Context context, int textViewResourceId, List<Student> objects){
        //重写了父类的构造函数
        //传入上下文，子布局的id,数据
        super(context,textViewResourceId,objects);
        resourceId=textViewResourceId;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent){
        Student student=getItem(position); //获取当前项的Student实例

        View view=LayoutInflater.from(getContext()).inflate(resourceId,parent,false);
        TextView studentname=(TextView) view.findViewById(R.id.student_name);//获取实例
        TextView studentid=(TextView) view.findViewById(R.id.student_ID);//获取实例
        TextView studentage=(TextView) view.findViewById(R.id.student_age);

        //在文本组件中显示信息
        studentname.setText(student.getName());
        studentid.setText(student.getID());
        studentage.setText(student.getAge());
        return view;    //将布局返回
    }


}
