var editor;

$(document).ready(function () {
    require.config({
        paths: {
            'vs': 'dev/vs'
        }
    });
    require(['vs/editor/editor.main'], function () {
        editor = monaco.editor.create(document.getElementById('coc-editor-body'), {
            language: 'python',
            scrollBeyondLastLine: false,
            theme: 'vs'
        });
    });

    $('.coc-editor-select-lang select').on('change', function () {
        window.monaco.editor.setModelLanguage(window.monaco.editor.getModels()[0], this.value) 
    });

    $('.coc-editor-select-theme select').on('change', function () {
        monaco.editor.setTheme(this.value);
    });

    $('#custom-inputs input').on('change', function() {
        if ($('#custom-inputs input').is(':checked')) {

        }
    })
});
