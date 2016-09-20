import mqtt from 'mqtt';
import uuid from 'uuid';


class APIService {  // CSM API Service, access to the CSM hight privilige api
  constructor(url) {
    this.id = uuid.v4();
    this.url = url;
    this.serviceTopic = `iottalk/api/req/gui-${this.id}`;
    this.dev = {
      pubTopic: `iottalk/api/req/gui-${this.id}/device`,
      subTopic: `iottalk/api/res/gui-${this.id}/device`,
      daList: undefined,
    };

    this.connect();

    console.log('client id', this.id);
  }

  connect() {
    const conn = this.conn = mqtt.connect(this.url, {
      will: this.willOption
    });

    // subscribe to `device` api
    this.conn.subscribe(this.dev.subTopic, {qos: 2}, () => {
      this.pub(this.dev.pubTopic, {'op': 'attach'});
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
    console.log('iottalk api service connected');
  }


  on_error(error) {
    console.error(error);
  }


  on_offline() {
    console.log('api handler gose offline');

    this.pub(this.serviceTopic, {'op': 'detach'});
  }


  on_close() {
    console.log('api handler mqtt connection closed');
  }


  on_message(topic, msg, packet) {
    const payload = JSON.parse(msg);
    
    console.log(topic, payload);

    if (payload.state !== 'ok') {
      console.error(payload);
      return;
    }

    if (topic === this.dev.subTopic) {
      return this.on_message_dev(payload, packet);
    }
  }


  on_message_dev(msg, packet) {
    const opcode = msg.op;
    if (opcode === 'attach') {
      this.dev.daList = msg.da_list;
    }
  }


  pub(topic, msg, options) {
    /* 
    :param payload: a json object

    :ref:`https://github.com/mqttjs/MQTT.js#mqttclientpublishtopic-message-options-callback`
    */
    return this.conn.publish(
      topic, 
      JSON.stringify(msg),
      options);
  }


  get willOption() {
    return {
      topic: `iottalk/api/req/gui-${this.id}`,
      payload: JSON.stringify({'op': 'detach'}),
    };
  }
}


export default {
  APIService: APIService,  // CSM API Service
}
