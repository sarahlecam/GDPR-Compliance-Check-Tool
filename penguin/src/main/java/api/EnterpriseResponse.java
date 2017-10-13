package api;

import com.fasterxml.jackson.annotation.JsonProperty;
import generated.tables.records.DatainfoRecord;
import generated.tables.records.ReceiptsRecord;

import java.math.BigDecimal;
import java.sql.Time;
import java.util.List;

/**
 * This is an API Object.  Its purpose is to model the JSON API that we expose.
 * This class is NOT used for storing in the Database.
 *
 * This ReceiptResponse in particular is the model of a Receipt that we expose to users of our API
 *
 * Any properties that you want exposed when this class is translated to JSON must be
 * annotated with {@link JsonProperty}
 */
public class EnterpriseResponse {
    @JsonProperty
    Integer id;

    @JsonProperty
    String dataType;

    @JsonProperty
    String reason;

    @JsonProperty
    Boolean shared;

    @JsonProperty
    String companyName;

    @JsonProperty
    String address;

    @JsonProperty
    String contact;

    @JsonProperty
    String website;

   public EnterpriseResponse(DatainfoRecord dbRecord) {
        this.dataType = dbRecord.getDatatype();
        this.reason = dbRecord.getReason();
        this.shared = dbRecord.getShared();
        this.id = dbRecord.getId();
        this.companyName = dbRecord.getCompanyname();
        this.address = dbRecord.getAddress();
        this.contact = dbRecord.getContact();
        this.website = dbRecord.getWebsite();

    }
}
