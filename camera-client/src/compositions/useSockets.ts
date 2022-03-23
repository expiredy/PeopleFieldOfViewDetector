import { io } from "socket.io-client"
const socketConnection = {
    socket: null as any
}

function connectSockets()  {
    socketConnection.socket = io("http://10.10.29.35:5000/");

    socketConnection.socket.onopen = () => {
        if (socketConnection.socket.readyState){
            socketConnection.socket.emit("hello", { name: "John" });

            console.log("[+] Websocket connect success")
        }
    }

    socketConnection.socket.onmessage = (event: any) => {
        const raw = JSON.parse(event.data)

        console.log("[+] Get websocket message")

        const {type, data} = raw
        console.log(type)
// socketConnection()
    }
}

connectSockets()

export const useSockets = () => {
    const send = ({types={}, params={}}) => {
        try {
            socketConnection.socket.send(JSON.stringify({
                types: types,
                params: params
            }))
        } catch {
            connectSockets();
        }
    }
}
