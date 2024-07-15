using System;
using System.Collections.Generic;
using System.Configuration;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AICode.Services
{

    public class BaseService
    {
        public string ApiUrl = GetApiUrl();    

        protected static string GetApiUrl()
        {
            ExeConfigurationFileMap configMap = new ExeConfigurationFileMap();
            configMap.ExeConfigFilename = Environment.CurrentDirectory + @"\AICode\app.config"; ;
            Configuration config = ConfigurationManager.OpenMappedExeConfiguration(configMap, ConfigurationUserLevel.None);
            var test = config.AppSettings.Settings["ApiUrl"].Value;
            return test;

        }
    }

}
