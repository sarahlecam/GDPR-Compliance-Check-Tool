package controllers;

import com.google.common.io.Resources;
import java.io.IOException;
import javax.ws.rs.*;
import javax.ws.rs.core.MediaType;

import static java.nio.charset.StandardCharsets.UTF_8;

@Path("/")
@Produces(MediaType.TEXT_HTML)
public class StaticHtmlController {

    @GET
    public String getIndexPage() throws IOException {
        Resources.getResource("index.html");
        return Resources.toString(Resources.getResource("index.html"), UTF_8);
    }

    @GET
    @Path("form/")
    public String getFormPage() throws IOException {
        Resources.getResource("testForm.html");
        return Resources.toString(Resources.getResource("testForm.html"), UTF_8);
    }

    @GET
    @Path("/notice/{companyName}")
    public String getNotice(@PathParam("companyName") String companyName) throws IOException {
        Resources.getResource("notice.html");
        return Resources.toString(Resources.getResource("notice.html"), UTF_8);
    }
}
