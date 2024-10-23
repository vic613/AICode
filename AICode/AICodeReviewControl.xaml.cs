using AICode.Models;
using AICode.Services;
using AICode.Utilities;
using System;
using System.Collections.Generic;
using System.Configuration;
using System.Diagnostics.CodeAnalysis;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;

namespace AICode
{
    /// <summary>
    /// Interaction logic for AICodeReviewControl.
    /// </summary>
    public partial class AICodeReviewControl : UserControl
    {

        /// <summary>
        /// Initializes a new instance of the <see cref="AICodeReviewControl"/> class.
        /// </summary>
        public AICodeReviewControl()
        {
            try
            {
                this.InitializeComponent();
                TabVisible();
                LoadModel();
            }
            catch (Exception ex) {
                CustomErrorLog.LogError(ex.Message);
            }
        }

        private void LoadModel()
        {
            cmbModel.Items.Add("llama3.1");
            cmbModel.Items.Add("AICode");          
            cmbModel.SelectedIndex = 0;
        }

        private void TabVisible()
        {
            try
            {
          
                if (AICodeSettings.Environment == "Prod")
                {
                    tiLogin.Visibility = Visibility.Hidden;
                    tiMain.Visibility = Visibility.Hidden;
                }
            }
            catch (Exception ex) {
                CustomErrorLog.LogError(ex.Message);
            }
        }

        /// <summary>
        /// Handles click on the button by displaying a message box.
        /// </summary>
        /// <param name="sender">The event sender.</param>
        /// <param name="e">The event args.</param>
        [SuppressMessage("Microsoft.Globalization", "CA1300:SpecifyMessageBoxOptions", Justification = "Sample code")]
        [SuppressMessage("StyleCop.CSharp.NamingRules", "SA1300:ElementMustBeginWithUpperCaseLetter", Justification = "Default event handler naming pattern")]
        private async void btnLogin_click(object sender, RoutedEventArgs e)
        {
            LoginService loginservice = new LoginService();
            LoginModel loginModel = new LoginModel();
            loginModel.username = txtUsername.Text;
            loginModel.password = txtPassword.Password.ToString();

            bool result = await loginservice.Login(loginModel);

            if (!result)
            {
                MessageBox.Show(
                    string.Format(System.Globalization.CultureInfo.CurrentUICulture, "Invoked '{0}'", this.ToString()),
                    "AICodeReview");
            }
            else
            {
                tabControl.SelectedIndex = 1;

            }
        }

        private async void btnReview_click(object sender, RoutedEventArgs e)
        {
            try
            {
                txtResult.Text = string.Empty;
                if (cmbModel.SelectedItem.ToString() == "AICode")
                {
                    CodeService codeservice = new CodeService();
                    CodeModel codeModel = new CodeModel();
                    codeModel.prompt = txtCurrent.Text;
                    CodeModel task = await codeservice.CodeReviewAsync(codeModel);
                    if (task.resultdata == null)
                    {
                        MessageBox.Show(
                            string.Format(System.Globalization.CultureInfo.CurrentUICulture, "Invoked '{0}'", this.ToString()),
                            "AICodeReview");
                    }
                    else
                    {
                        txtResult.Text = task.ToString();

                    }

                }
                else if (cmbModel.SelectedItem.ToString() == "llama3.1")
                {
                    ExternalCodeService codeservice = new ExternalCodeService();
                    ExternalCodeModel codeModel = new ExternalCodeModel();
                    codeModel.prompt = txtCurrent.Text;
                    codeModel.model = "llama3.1";

                    ExternalCodeModel task = await codeservice.ExternalCodeReviewAsync(codeModel);
                    if (task.response == null)
                    {
                        MessageBox.Show(
                            string.Format(System.Globalization.CultureInfo.CurrentUICulture, "Invoked '{0}'", this.ToString()),
                            "AICodeReview");
                    }
                    else
                    {
                        txtResult.Text = task.response.ToString();

                    }
                }
            }
            catch (Exception ex)
            {
                CustomErrorLog.LogError(ex.Message);
            }



        }



    }
}