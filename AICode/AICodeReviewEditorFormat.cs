using Microsoft.VisualStudio.Text.Classification;
using Microsoft.VisualStudio.Utilities;
using System.ComponentModel.Composition;
using System.Windows.Media;

namespace AICode
{
    /// <summary>
    /// Defines an editor format for the AICodeReviewEditor type that has a purple background
    /// and is underlined.
    /// </summary>
    [Export(typeof(EditorFormatDefinition))]
    [ClassificationType(ClassificationTypeNames = "AICodeReviewEditor")]
    [Name("AICodeReviewEditor")]
    [UserVisible(true)] // This should be visible to the end user
    [Order(Before = Priority.Default)] // Set the priority to be after the default classifiers
    internal sealed class AICodeReviewEditorFormat : ClassificationFormatDefinition
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="AICodeReviewEditorFormat"/> class.
        /// </summary>
        public AICodeReviewEditorFormat()
        {
            //this.DisplayName = "AICodeReviewEditor"; // Human readable version of the name
            //this.BackgroundColor = Colors.White;
            //this.TextDecorations = System.Windows.TextDecorations.Underline;
        }
    }
}
