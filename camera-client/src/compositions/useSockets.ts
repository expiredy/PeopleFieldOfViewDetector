import { io } from "socket.io-client";

const socket_connection = {
    socket: null as any
}


export const connectSokcets = () => {
    socket_connection.socket = io("wss://10.10.29.35:5000/");
}