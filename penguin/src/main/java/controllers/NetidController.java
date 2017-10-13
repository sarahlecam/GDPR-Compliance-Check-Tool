package controllers;

import javax.ws.rs.*;


@Path("/netid")
public class NetidController {

    @GET
    public String getNetid()
    {
        return "as3664";
    }

}
