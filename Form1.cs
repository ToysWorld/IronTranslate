using System;
using System.IO;
using System.Windows.Forms;

namespace NoTs
{
    public partial class Form1 : Form
    {
        string local = Application.StartupPath;

        public Form1()
        {
            InitializeComponent();
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            //避免写空导致Python犯傻
            if (textBox1.Text != string.Empty) { StreamWriter sw = new StreamWriter(local + "\\will.txt"); sw.Write(textBox1.Text);sw.Flush();sw.Close();}
            

            //翻译
            System.Diagnostics.Process.Start(local + "\\fy.exe");



        }

        public void read()
        {
            StreamReader sw = new StreamReader(local + "\\result.txt");
            string result = sw.ReadToEnd();
            textBox2.Text = result;
            sw.Close();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            read();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            textBox1.Text = string.Empty;
            textBox2.Text = string.Empty;
        }
    }
}
