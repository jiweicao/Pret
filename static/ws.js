String.prototype.format = function (){var d=this.toString();if(!arguments.length)return d;var a="string"==typeof arguments[0]?arguments:arguments[0],c;for(c in a)d=d.replace(RegExp("\\{"+c+"\\}","gi"),a[c]);return d};

$(document).ready(function() {
    if (!window.console) window.console = {};
    if (!window.console.log) window.console.log = function() {};

    $("#addurl").click(function(){
        newMessage({"command":"search", "query":$("#url").val()});
        return false;
    });

    $("#url").keypress(function(event) {
        newMessage({"command":"search", "query":$("#url").val()});
    });
    
    updater.start();
});

function newMessage(message) {
      updater.socket.send(JSON.stringify(message));
};

var updater = {
    socket: null,

    start: function() {
        var url = "ws://" + location.host + "/ws";

        if ("WebSocket" in window) {
	    updater.socket = new WebSocket(url);
        } else {
            updater.socket = new MozWebSocket(url);
        }
	updater.socket.onmessage = function(event) {
            msg = JSON.parse(event.data)
            console.log("Got msg:")
            console.log(msg)
            dispathcer[msg.command](msg.arg)
	}
    },
};