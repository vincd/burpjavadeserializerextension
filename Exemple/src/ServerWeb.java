import java.io.*;
import java.net.*;
import java.util.zip.DeflaterOutputStream;
import java.util.zip.InflaterInputStream;
import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpServer;


public class ServerWeb {

  public static void main(String[] arg) throws Exception {

    HttpServer server = HttpServer.create(new InetSocketAddress(12345), 0);
    server.createContext("/", new MyHandler());
    server.setExecutor(null);
    server.start();
  }


  public static class MyHandler implements HttpHandler {
    @Override
    public void handle(HttpExchange t) throws IOException {

      Employee employee = null;

      System.out.println("Server Waiting");

      InputStream in = t.getRequestBody();
      
      InflaterInputStream localInflaterInputStream = new InflaterInputStream(in);
      ObjectInputStream localObjectInputStream = new ObjectInputStream(localInflaterInputStream);
      

      try {
        employee = (Employee )localObjectInputStream.readObject();
      } catch (Exception e) {System.out.println(e); }
      
      System.out.println("Server Received employeeNumber= "
                            + employee .getEmployeeNumber());
      System.out.println("Server Received employeeName= "
                            + employee .getEmployeeName() + "\n");

      employee .setEmployeeNumber(256);
      employee .setEmployeeName("John");
      System.out.println("Server Sent employeeNumber= "
                            + employee .getEmployeeNumber());
      System.out.println("Server Sent employeeName= "
                            + employee .getEmployeeName() +"\n");

      t.sendResponseHeaders(200, 0);
      
      OutputStream os = t.getResponseBody();
      DeflaterOutputStream localDeflaterOutputStream = new DeflaterOutputStream(os);
      ObjectOutputStream localObjectOutputStream = new ObjectOutputStream(localDeflaterOutputStream);
      
      
      localObjectOutputStream.writeObject(employee);
      
      localObjectInputStream.close();
      localObjectOutputStream.close();
    }
  }

}
