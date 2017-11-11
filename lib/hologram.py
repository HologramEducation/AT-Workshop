# format message for Hologram's server
def formatMsg(msg, key):
    msg.replace("\"","\\\"");
    return "{\"k\": \"" + key + "\", \"d\": \"" + msg + "\"}\r\n";

# hologram's data engine cloud IP address
def ip():
    return "23.253.146.203"

# hologram's data engine cloud port
def port():
    return "9999"
