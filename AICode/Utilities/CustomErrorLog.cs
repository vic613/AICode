using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AICode.Utilities
{
    public static class CustomErrorLog
    {
        public static void LogError(string message)
        {

            using (EventLog eventLog = new EventLog("Application"))
            {
                eventLog.Source = "AICode";
                eventLog.WriteEntry(message, EventLogEntryType.Error, 101, 1);
            }
        }
    }
}
