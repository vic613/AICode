using AICode.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http;
using System.Net;
using System.Text;
using System.Threading.Tasks;
using AICode.Utilities;

namespace AICode.Services
{
    public class CodeService : BaseService
    {
        static CustomHttpClient client = new CustomHttpClient();
        public async Task<CodeModel> CodeReviewAsync(CodeModel codeModel)
        {

            try
            {
                var client = new HttpClient();
 
                string jsonContent = System.Text.Json.JsonSerializer.Serialize(codeModel);

                StringContent content = new StringContent(jsonContent, System.Text.Encoding.UTF8, "application/json");

                HttpResponseMessage response = await client.PostAsync(ApiUrl + "/codeapi/codereview", content);
                if (response.StatusCode == HttpStatusCode.OK)
                {
                    CodeModel result = new CodeModel();
                    result.resultdata = response.Content.ReadAsStringAsync().Result.ToString();
                    return result;
                }
                else
                {
                    CodeModel result = new CodeModel();
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

        public async Task<CodeModel> CodeReview(CodeModel codeModel)
        {

            try
            {
                var client = new HttpClient();

                string jsonContent = System.Text.Json.JsonSerializer.Serialize(codeModel);

                StringContent content = new StringContent(jsonContent, System.Text.Encoding.UTF8, "application/json");

                HttpResponseMessage response = await client.PostAsync(ApiUrl + "/externalcodeapi/codereview", content);
                if (response.StatusCode == HttpStatusCode.OK)
                {
                    CodeModel result = new CodeModel();
                    result.resultdata = response.Content.ReadAsStringAsync().Result.ToString();
                    return result;
                }
                else
                {
                    CodeModel result = new CodeModel();
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

