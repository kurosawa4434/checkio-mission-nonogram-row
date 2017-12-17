//Dont change it
requirejs(['ext_editor_io', 'jquery_190', 'raphael_210'],
    function (extIO, $, TableComponent) {

        function nonogramRowCanvas(dom, dataInp, expl){
        }

        var $tryit;
        var io = new extIO({
            multipleArguments: false,
            functions: {
                js: 'nonogramRow',
                python: 'nonogram_row'
            },
            /*
            animation: function($expl, data){
                barcodeReaderCanvas($expl[0],
                    data.in, data.ext.explanation);
            }
            */
        });
        io.start();
    }
);
