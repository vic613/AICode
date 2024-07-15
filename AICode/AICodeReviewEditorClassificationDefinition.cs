using Microsoft.VisualStudio.Text.Classification;
using Microsoft.VisualStudio.Utilities;
using System.ComponentModel.Composition;

namespace AICode
{
    /// <summary>
    /// Classification type definition export for AICodeReviewEditor
    /// </summary>
    internal static class AICodeReviewEditorClassificationDefinition
    {
        // This disables "The field is never used" compiler's warning. Justification: the field is used by MEF.
#pragma warning disable 169

        /// <summary>
        /// Defines the "AICodeReviewEditor" classification type.
        /// </summary>
        [Export(typeof(ClassificationTypeDefinition))]
        [Name("AICodeReviewEditor")]
        private static ClassificationTypeDefinition typeDefinition;

#pragma warning restore 169
    }
}
