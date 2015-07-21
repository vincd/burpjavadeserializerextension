import java.io.*;
import java.net.*;
import java.net.URL;
import java.util.zip.DeflaterOutputStream;
import java.util.zip.InflaterInputStream;
import java.net.HttpURLConnection;

public class ClientWeb {

   public static void main(String[] arg) {
      try {
         Employee joe = new Employee(150, "Joe");

         System.out.println("Client Sent employeeNumber= "
                            + joe .getEmployeeNumber());
         System.out.println("Client Sent employeeName= "
                            + joe .getEmployeeName() + "\n");

          
          URL localURL = new URL("http", "kali", 12345, "/");
          HttpURLConnection localURLConnection = (HttpURLConnection) localURL.openConnection();
          
          localURLConnection.setDoOutput(true);
          localURLConnection.setDoInput(true);
          localURLConnection.setRequestProperty("Content-Type", "application/octet-stream");
          
          DeflaterOutputStream localDeflaterOutputStream = new DeflaterOutputStream(localURLConnection.getOutputStream());
          ObjectOutputStream localObjectOutputStream = new ObjectOutputStream(localDeflaterOutputStream);

            
         // send to server
         localObjectOutputStream.writeObject(joe);
         localObjectOutputStream.flush();
         localObjectOutputStream.close();
         localObjectOutputStream = null;
         
         
         InputStream localInputStream = null;
         localInputStream = localURLConnection.getInputStream();
         
         
         InflaterInputStream localInflaterInputStream = new InflaterInputStream(localInputStream);
         ObjectInputStream localObjectInputStream = new ObjectInputStream(localInflaterInputStream);
         
         
         joe= (Employee)localObjectInputStream.readObject();
         localObjectInputStream.close();
         
         
         // print received results
         System.out.println("Client Received employeeNumber= "
                            + joe .getEmployeeNumber());
         System.out.println("Client Received employeeName= "
                            + joe .getEmployeeName());

      } catch (Exception e) {System.out.println(e); }
   }
}