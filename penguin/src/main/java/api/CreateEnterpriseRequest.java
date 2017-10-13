package api;

import org.hibernate.validator.constraints.NotEmpty;

import java.math.BigDecimal;

/**
 * This is an API Object.  It's job is to model and document the JSON API that we expose
 *
 * Fields can be annotated with Validation annotations - these will be applied by the
 * Server when transforming JSON requests into Java objects IFF you specify @Valid in the
 * endpoint.  See {@link controllers.EnterpriseController#createEnterprise(CreateEnterpriseRequest)} for
 * and example.
 */
public class CreateEnterpriseRequest {
    @NotEmpty
    public String companyName;

    public String dataType;

    public String reason;

    public Boolean shared;

    public String address;

    public String contact;

    public String website;

}
