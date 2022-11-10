export default{
    methods:{
        sendReq: async function (url, method, data = null) {
            try {
              
              const headers = {};
              let body
              if (data){
                  // headers['Content-type'] = 'application/json'
                  // headers['Access-Control-Allow-Origin'] = 'http://localhost:8000'
                  // headers['Access-Control-Allow-Credentials'] = true
                  headers.append('Content-Type', 'application/json');
                  headers.append('Accept', 'application/json');
                  headers.append('Origin','http://localhost:8000');
                  body = JSON.stringify(data)
              }
              var resBody;

              const res = await fetch(url, {
                method,
                headers,
                body,
              });
              if (res.status === 200 || res.status === 201){
                resBody = await res.json();
              }else{
                resBody = 'error'
              }
              return resBody
            } catch (error) {
              resBody = 'error'
              return resBody
            }
          },
    }
}