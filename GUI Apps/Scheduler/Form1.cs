using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Scheduler
{
    public partial class Calendar : Form
    {
        public Calendar()
        {
            InitializeComponent();
        }

        public void Scheduler()
        {
            int days = 7;
            int hours = 8;
            string [,] week = new string[days, hours];  //might work?
        }

        private void Calendar_Load(object sender, EventArgs e){}

        private void SubmitBtn_Click(object sender, EventArgs e)
        {

        }
    }
}
