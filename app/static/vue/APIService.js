import mqtt from 'mqtt';


class BaseAPIService {
  constructor(url) {
    this.pubTopic = undefined;
    this.subTopic = undefined;
    
    this.url = url;
  }

  connect() {
    const conn = this.conn = mqtt.connect(this.url, {
      // keepalive: 10000,
      will: this.willOption
    });

    conn.on('connect', () => {
      this.on_connect();
    });
    conn.on('close', () => {
      this.on_close();
    });
    conn.on('offline', () => {
      this.on_offline();
    });
    conn.on('error', (...args) => {
      this.on_error(...args);
    });
    conn.on('message', (...args) => {
      this.on_message(...args);
    });
  }


  on_connect() {
    this.conn.subscribe(this.subTopic, {qos: 2}, () => {
      this.pub({'op': 'attach'});
    });
  }


  on_error(error) {
    console.error(error);
  }


  on_offline() {
    console.log('api handler gose offline');

    this.pub({'op': 'detach'});
  }


  on_close() {
    console.log('api handler mqtt connection closed');
  }


  on_message(topic, msg, packet) {
    const payload = JSON.parse(msg);
    
    console.log(payload);
  }


  pub(msg, options) {
    /* 
    :param payload: a json object

    :ref:`https://github.com/mqttjs/MQTT.js#mqttclientpublishtopic-message-options-callback`
    */
    return this.conn.publish(
      this.pubTopic, 
      JSON.stringify(msg),
      options);
  }


  get willOption() {
    return {
      topic: this.pubTopic,
      payload: JSON.stringify({'op': 'detach'}),
    };
  }
}


class DeviceAPI extends BaseAPIService {
  constructor(...args) {
    super(...args);

    this.pubTopic = 'iottalk/api/req/gui/device';
    this.subTopic = 'iottalk/api/res/gui/device';
    this.daList= undefined;

    this.connect();
  }


  on_connect() {
    console.log('device api mqtt connected');
    
    super.on_connect();
  }


  on_close() {
    console.log('device api mqtt disconnted');

    super.on_close();
  }


  on_message(topic, msg, packet) {
    const payload = JSON.parse(msg);
    
    console.log('msg', payload);

    if (payload.state !== 'ok') {
      console.error(payload);
      return;
    }

    const opcode = payload.op;
    if (opcode === 'attach') {
      this.daList = payload.da_list;
    }
  }
}


export default {
  DeviceAPI: DeviceAPI,
}
