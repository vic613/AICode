using AICode.Models;
using AICode.Utilities;
using Microsoft.Internal.VisualStudio.PlatformUI;
using Newtonsoft.Json.Linq;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Runtime;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;
using static System.Windows.Forms.VisualStyles.VisualStyleElement.StartPanel;

namespace AICode.Services
{
    public class LoginService : BaseService
    {
        static CustomHttpClient client = new CustomHttpClient();
        public async Task<bool> Login(LoginModel loginModel)
        {

            try
            {
                var client = new HttpClient();

                string jsonContent = System.Text.Json.JsonSerializer.Serialize(loginModel);

                StringContent content = new StringContent(jsonContent, System.Text.Encoding.UTF8, "application/json");

                HttpResponseMessage response = await client.PostAsync(ApiUrl + "/loginapi/login", content);
                return response.StatusCode == HttpStatusCode.OK;

            }
            catch (Exception e)
            {
                return false;

            }



        }
    }
}
