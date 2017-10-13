package dao;

import generated.tables.records.DatainfoRecord;
import org.jooq.Configuration;
import org.jooq.DSLContext;
import org.jooq.impl.DSL;

import java.util.ArrayList;
import java.util.List;

import static com.google.common.base.Preconditions.checkState;
import static generated.Tables.DATAINFO;
import static generated.Tables.RECEIPTS;

public class EnterpriseDao {
    DSLContext dsl;

    public EnterpriseDao(Configuration jooqConfig) {
        this.dsl = DSL.using(jooqConfig);
    }

    public int insert(String dataType, String reason, Boolean shared, String companyName) {
        DatainfoRecord datainfoRecord = dsl
                .insertInto(DATAINFO, DATAINFO.DATATYPE, DATAINFO.REASON, DATAINFO.SHARED, DATAINFO.COMPANYNAME)
                .values(dataType,reason,shared,companyName)
                .returning(RECEIPTS.ID)
                .fetchOne();

        checkState(datainfoRecord != null && datainfoRecord.getId() != null, "Insert failed");

        return datainfoRecord.getId();
    }

    public List<DatainfoRecord> getAllDataInfo(String companyName) {
        List<DatainfoRecord> dataInfoResponseList = dsl.selectFrom(DATAINFO).where(DATAINFO.COMPANYNAME.eq(companyName)).fetch();

        if (dataInfoResponseList == null || dataInfoResponseList.size() < 1) {
            System.out.println("did not find any receipts");
            return new ArrayList<>();

        }
        return dataInfoResponseList;
    }
}
