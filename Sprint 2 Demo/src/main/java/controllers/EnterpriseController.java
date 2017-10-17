package controllers;

import api.CreateEnterpriseRequest;
import api.EnterpriseResponse;
import dao.EnterpriseDao;
import generated.tables.records.DatainfoRecord;
import javax.validation.Valid;
import javax.validation.constraints.NotNull;
import javax.ws.rs.*;
import javax.ws.rs.core.MediaType;
import java.util.List;

import static java.util.stream.Collectors.toList;

@Path("")
@Consumes(MediaType.APPLICATION_JSON)
@Produces(MediaType.APPLICATION_JSON)
public class EnterpriseController {
    final EnterpriseDao enterpriseDao;

    public EnterpriseController(EnterpriseDao enterpriseDao) {
        this.enterpriseDao = enterpriseDao;
    }

    @POST
    public int createReceipt(@Valid @NotNull CreateEnterpriseRequest enterprise) {

        return enterpriseDao.insert(enterprise.dataType,enterprise.reason, enterprise.shared,enterprise.companyName,enterprise.address,enterprise.contact,enterprise.website,enterprise.dopName,enterprise.dopContact,enterprise.companyType);
    }

    @GET
    @Path("/{company}")
    public List<EnterpriseResponse> getDataInfo(@PathParam("company") String companyName) {
        List<DatainfoRecord> dataInfo = enterpriseDao.getAllDataInfo(companyName);
        return dataInfo.stream().map(EnterpriseResponse::new).collect(toList());
    }

    @DELETE
    @Path("/")
    public void deleteEnterprise() {
        enterpriseDao.deleteAll();
    }
}
