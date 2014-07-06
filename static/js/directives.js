angular.module('tikoApp.directives',[])
    .directive('tkCanvas', ['$interval', '$http', function ($interval, $http) {

        return {
            restrict:'E',
            template:'<canvas style="width:100%;height:100%;">Please talk to tiko ruff</canvas>',
            link: function (scope, element, attributes) {
                var url = attributes.tkSrc,
                    fps = parseFloat(attributes.tkFps || 25),
                    canvas = element.find('canvas')[0]
                    context = canvas.getContext('2d');

                context.canvas.width  = window.innerWidth;
                context.canvas.height = window.innerHeight;

                var l = {
                    x:100,
                    y:100
                }

                $interval(function () {
                    $http
                        .get(url)
                        .success(function (data) {
                            scope.error = undefined;
                            console.log(data);
                            context.clearRect(0, 0, canvas.width, canvas.height);
                            for (var i = 0; i < (data.displayObjects || []).length; i++)
                                draw(data.displayObjects[i], context);

                        })
                        .error(function () {
                           scope.error = 'Hi Ruff, the app isn\'t currently running. Press the play button in IntelliJ\
                           on the top right corner';
                        });
                }, 1000/fps);
            }
        }
    }]);

function nop(){};

function draw(data, context) {
    if (!data || !context)
        return;
    var type = data.type,
        visualData = data.description;

    switch (type) {
        case ('line'):
            context.beginPath();
            context.moveTo(visualData.start.x, visualData.start.y);
            context.strokeStyle = visualData.strokeStyle || 'black';
            context.lineTo(visualData.end.x, visualData.end.x);
            context.stroke();
            break;
        case ('rect'):
            context.beginPath();
            context.lineWidth = visualData.lineWidth || '1';
            context.strokeStyle = visualData.strokeStyle || 'black';
            context.fillStyle = visualData.fillStyle || 'white';
            if (visualData.fill)
                context.fillRect(visualData.start.x,visualData.start.y,visualData.end.x,visualData.end.y);
            else
                context.rect(visualData.start.x,visualData.start.y,visualData.end.x,visualData.end.y);
            context.stroke();
    }
}