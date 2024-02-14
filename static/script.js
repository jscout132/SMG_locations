        require([
          "esri/config", 
          "esri/WebMap",
          "esri/views/MapView", 
          "esri/widgets/ScaleBar",
          "esri/widgets/Legend"
        ], function(esriConfig, WebMap, MapView, ScaleBar, Legend) {

            esriConfig.apiKey = "AAPKd763eac44500457da17f03e1a85cdbeetAgzrp5T6j_n46KVX-ej-2PUEHpJ1VhP8gNzZn4qzP4EYA7ai9zuOUr_9vBVQtLH";
            
            const webmap = new WebMap({
              portalItem: {
                id: "2fe2d6d3d98948dc9e127eed3e1dba5c"
              }
            });

            const view = new MapView({
                map: webmap,
                container: "viewDiv" // Div element
            });

        });