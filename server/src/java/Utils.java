import java.io.*;
import java.util.*;
import java.lang.*;

// Class made as a hack to make a method to read the policy and use it in python
// Use this class to implement any extra method to interact with the POMDP in Java

class Utils {

    public static POMDP readPolicy(String spuddfile, String policyfile){
	POMDP pomdp = new POMDP(spuddfile);
	// Read from disk using FileInputStream.
	FileInputStream f_in;
	try {
	    f_in = new FileInputStream (policyfile);
	} catch (FileNotFoundException err) {
	    System.out.println("file not found error "+err);
	    return pomdp;
	}
	Object obj;
	ObjectInputStream obj_in;
	try {
		    
	    // Read object using ObjectInputStream.
	    obj_in = new ObjectInputStream (f_in);
	} catch (IOException err) {
	    System.out.println("file read error"+err);
	    return pomdp;
	} 
	try {
	    // Read an object.
	    obj = obj_in.readObject ();
	} catch (IOException err) {
	    System.out.println("file read error"+err);
	    return pomdp;
	} catch (ClassNotFoundException err) {
	    System.out.println("class error"+err);
	    return pomdp;
	} 
	boolean heuristic=false;
	// Is the object that you read in, say, an instance
	// of the POMDP class?
	if (obj instanceof POMDP) {
	    // Cast object to a POMDP
	    pomdp = (POMDP) obj;
		    
	    // Do something with pomdp
	    //now we have to get all the global information and variable name
	    // stuff from a file
	    // this will stomp over some stuff in the above read, but works
	    pomdp.readFromFile(spuddfile);
	    /*
	      pomdp.actions[0].transFn[0].display();
	      pomdp.actions[0].transFn[1].display();
	      pomdp.actions[0].transFn[2].display();
		    
	      DD tmp = OP.mult(pomdp.actions[0].transFn[1],pomdp.actions[0].transFn[2]);
	      tmp = OP.mult(tmp,pomdp.actions[0].obsFn[1]);
	      tmp.display();
	    */
	    //pomdp.displayPolicy();
	    //pomdp.addbeldiff = true;
	    //System.out.println("addbeldiff is "+pomdp.addbeldiff);
		    
	    //    double [] obsfit = pomdp.evaluateObservations(1);
	    //for (int i =0; i<obsfit.length; i++) 
	    //System.out.println("fitness of "+i+":"+obsfit[i]);
	    //double v0 = pomdp.evaluatePolicyStationary(30,30);
	    //System.out.println("value is "+v0);


	    // evaluate the policy
	    //double polval = pomdp.evaluatePolicyStationary(1,100,true);
	    //System.out.println("policy value is "+polval);
    
	}
	
	return pomdp;
    }

    public static Object deepCopy(Object object) {
	try {
	    ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
	    ObjectOutputStream outputStrm = new ObjectOutputStream(outputStream);
	    outputStrm.writeObject(object);
	    ByteArrayInputStream inputStream = new ByteArrayInputStream(outputStream.toByteArray());
	    ObjectInputStream objInputStream = new ObjectInputStream(inputStream);
	    return objInputStream.readObject();
	}
	catch (Exception e) {
	    e.printStackTrace();
	    return null;
	}
    }
}
