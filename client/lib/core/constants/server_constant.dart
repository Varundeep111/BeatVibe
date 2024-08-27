import 'dart:io';

class ServerConstant {
  static String serverURL = Platform.isAndroid
      ? 'http://192.168.171.132:8080'
      : "http://127.0.0.1:8080";
}
