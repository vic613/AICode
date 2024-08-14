using AICode.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http;
using System.Net;
using System.Text;
using System.Threading.Tasks;
using AICode.Utilities;
using Newtonsoft.Json.Linq;
using System.Text.Json.Nodes;
using EnvDTE;
using System.Text.Json;
using Newtonsoft.Json;


namespace AICode.Services
{
    public class ExternalCodeService : BaseService
    {
        static CustomHttpClient client = new CustomHttpClient();

        public async Task<ExternalCodeModel> ExternalCodeReviewAsync(ExternalCodeModel codeModel)
        {

            try
            {

                string jsonContent = System.Text.Json.JsonSerializer.Serialize(codeModel);

                StringContent content = new StringContent(jsonContent, System.Text.Encoding.UTF8, "application/json");
                //client.Timeout = TimeSpan.FromMinutes(90);
                HttpResponseMessage response = await client.PostAsync(ApiUrl + "/externalcodeapi/externalcodereview", content);
                if (response.StatusCode == HttpStatusCode.OK)
                {
                    ExternalCodeModel result = new ExternalCodeModel();
                    JObject obj = JObject.Parse(response.Content.ReadAsStringAsync().Result.ToString());
                    JToken data = obj.SelectToken("$.data");
                    result = JsonConvert.DeserializeObject<ExternalCodeModel>(data.ToString());

                    return result;
                }
                else
                {
                    ExternalCodeModel result = new ExternalCodeModel();
                    result.resultdata = "";
                    return result;
                }

;

            }
            catch (Exception ex)
            {
                throw ex;

            }



        }

    }
}

