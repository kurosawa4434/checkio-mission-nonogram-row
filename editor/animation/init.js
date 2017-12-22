//Dont change it
requirejs(['ext_editor_io', 'jquery_190', 'raphael_210'],
    function (extIO, $, TableComponent) {
        function nonogramRowCanvas(dom, dataInp, expl, answer_string){

            const
                color = {
                    dark: "#294270",
                    empty: "#FFFFFF",
                    unknown: "#8FC7ED",
                    filled: "#308AC0",
                },
                attr = {
                    rect: {
                        'stroke': color.dark,
                        'stroke-width': 1
                    },
                    text: {
                        clue: {
                            'stroke-width': 0,
                            'fill': color.dark,
                            "font-size": 14,
                            'font-family': "Verdana",
                            'text-anchor': "end",
                        },
                    }
                };

            const row_string = dataInp[0];
            const cell_length = row_string.length;
            const clue_numbers = dataInp[1].join(',');
            const h_margin = 50;
            const top_margin = 5;
            const cell_size = 15;

            const paper = Raphael(dom,
                             cell_size*cell_length+h_margin*2, 
                             cell_size + top_margin+2, 0, 0);

            const cell_color = {
                'O': color.filled,
                'X': color.empty,
                '?': color.unknown,
            };

            let cell_set = paper.set();

            for (let j=0; j < cell_length; j += 1) {

                cell_set.push(
                    paper.rect(j * cell_size + h_margin, top_margin,
                        cell_size,
                        cell_size).attr(attr.rect).attr(
                            "fill",
                            cell_color[row_string.slice(j,j+1)]
                        )
                );

                paper.text(h_margin-7, top_margin+7,
                    clue_numbers).attr(attr.text.clue);
            }

            const delay = 400

            setTimeout(function () {
                for (let k=0; k < cell_length; k += 1) {
                    cell_set[k].animate(
                        {'fill': cell_color[answer_string.slice(k,k+1)]},
                        delay*3
                    );
                }
            }(), delay*10);

            return
        }

        let $tryit;
        let io = new extIO({
            multipleArguments: false,
            functions: {
                js: 'nonogramRow',
                python: 'nonogram_row'
            },
            animation: function($expl, data){
                nonogramRowCanvas(
                    $expl[0],
                    data.in,
                    data.ext.explanation,
                    data.ext.answer
                );
            }
        });
        io.start();
    }
);
