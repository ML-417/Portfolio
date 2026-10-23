namespace Scheduler
{
    partial class Calendar
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.SchedulingDGrid = new System.Windows.Forms.DataGridView();
            this.ColumnMonday = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.ColumnTuesday = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.ColumnWednesday = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.ColumnThursday = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.ColumnFriday = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.ColumnSaturday = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.ColumnSunday = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.TaskTbx = new System.Windows.Forms.TextBox();
            this.SubmitBtn = new System.Windows.Forms.Button();
            this.TimeNud = new System.Windows.Forms.NumericUpDown();
            ((System.ComponentModel.ISupportInitialize)(this.SchedulingDGrid)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.TimeNud)).BeginInit();
            this.SuspendLayout();
            // 
            // SchedulingDGrid
            // 
            this.SchedulingDGrid.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.SchedulingDGrid.Columns.AddRange(new System.Windows.Forms.DataGridViewColumn[] {
            this.ColumnMonday,
            this.ColumnTuesday,
            this.ColumnWednesday,
            this.ColumnThursday,
            this.ColumnFriday,
            this.ColumnSaturday,
            this.ColumnSunday});
            this.SchedulingDGrid.Location = new System.Drawing.Point(248, 267);
            this.SchedulingDGrid.Name = "SchedulingDGrid";
            this.SchedulingDGrid.RowHeadersWidth = 62;
            this.SchedulingDGrid.RowTemplate.Height = 28;
            this.SchedulingDGrid.Size = new System.Drawing.Size(1116, 349);
            this.SchedulingDGrid.TabIndex = 1;
            // 
            // ColumnMonday
            // 
            this.ColumnMonday.HeaderText = "Monday";
            this.ColumnMonday.MinimumWidth = 8;
            this.ColumnMonday.Name = "ColumnMonday";
            this.ColumnMonday.ReadOnly = true;
            this.ColumnMonday.Resizable = System.Windows.Forms.DataGridViewTriState.True;
            this.ColumnMonday.Width = 150;
            // 
            // ColumnTuesday
            // 
            this.ColumnTuesday.HeaderText = "Tuesday";
            this.ColumnTuesday.MinimumWidth = 8;
            this.ColumnTuesday.Name = "ColumnTuesday";
            this.ColumnTuesday.ReadOnly = true;
            this.ColumnTuesday.Width = 150;
            // 
            // ColumnWednesday
            // 
            this.ColumnWednesday.HeaderText = "Wednesday";
            this.ColumnWednesday.MinimumWidth = 8;
            this.ColumnWednesday.Name = "ColumnWednesday";
            this.ColumnWednesday.ReadOnly = true;
            this.ColumnWednesday.Width = 150;
            // 
            // ColumnThursday
            // 
            this.ColumnThursday.HeaderText = "Thursday";
            this.ColumnThursday.MinimumWidth = 8;
            this.ColumnThursday.Name = "ColumnThursday";
            this.ColumnThursday.ReadOnly = true;
            this.ColumnThursday.Width = 150;
            // 
            // ColumnFriday
            // 
            this.ColumnFriday.HeaderText = "Friday";
            this.ColumnFriday.MinimumWidth = 8;
            this.ColumnFriday.Name = "ColumnFriday";
            this.ColumnFriday.ReadOnly = true;
            this.ColumnFriday.Width = 150;
            // 
            // ColumnSaturday
            // 
            this.ColumnSaturday.HeaderText = "Saturday";
            this.ColumnSaturday.MinimumWidth = 8;
            this.ColumnSaturday.Name = "ColumnSaturday";
            this.ColumnSaturday.ReadOnly = true;
            this.ColumnSaturday.Width = 150;
            // 
            // ColumnSunday
            // 
            this.ColumnSunday.HeaderText = "Sunday";
            this.ColumnSunday.MinimumWidth = 8;
            this.ColumnSunday.Name = "ColumnSunday";
            this.ColumnSunday.ReadOnly = true;
            this.ColumnSunday.Width = 150;
            // 
            // TaskTbx
            // 
            this.TaskTbx.Location = new System.Drawing.Point(465, 702);
            this.TaskTbx.Name = "TaskTbx";
            this.TaskTbx.Size = new System.Drawing.Size(250, 26);
            this.TaskTbx.TabIndex = 2;
            // 
            // SubmitBtn
            // 
            this.SubmitBtn.AllowDrop = true;
            this.SubmitBtn.Location = new System.Drawing.Point(956, 698);
            this.SubmitBtn.Name = "SubmitBtn";
            this.SubmitBtn.Size = new System.Drawing.Size(84, 37);
            this.SubmitBtn.TabIndex = 3;
            this.SubmitBtn.Text = "Submit";
            this.SubmitBtn.UseVisualStyleBackColor = true;
            // 
            // TimeNud
            // 
            this.TimeNud.Location = new System.Drawing.Point(779, 703);
            this.TimeNud.Name = "TimeNud";
            this.TimeNud.Size = new System.Drawing.Size(120, 26);
            this.TimeNud.TabIndex = 4;
            // 
            // Calendar
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1553, 925);
            this.Controls.Add(this.TimeNud);
            this.Controls.Add(this.SubmitBtn);
            this.Controls.Add(this.TaskTbx);
            this.Controls.Add(this.SchedulingDGrid);
            this.Name = "Calendar";
            this.Text = "Calendar";
            this.Load += new System.EventHandler(this.Calendar_Load);
            ((System.ComponentModel.ISupportInitialize)(this.SchedulingDGrid)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.TimeNud)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.DataGridView SchedulingDGrid;
        private System.Windows.Forms.DataGridViewTextBoxColumn ColumnMonday;
        private System.Windows.Forms.DataGridViewTextBoxColumn ColumnTuesday;
        private System.Windows.Forms.DataGridViewTextBoxColumn ColumnWednesday;
        private System.Windows.Forms.DataGridViewTextBoxColumn ColumnThursday;
        private System.Windows.Forms.DataGridViewTextBoxColumn ColumnFriday;
        private System.Windows.Forms.DataGridViewTextBoxColumn ColumnSaturday;
        private System.Windows.Forms.DataGridViewTextBoxColumn ColumnSunday;
        private System.Windows.Forms.TextBox TaskTbx;
        private System.Windows.Forms.Button SubmitBtn;
        private System.Windows.Forms.NumericUpDown TimeNud;
    }
}

