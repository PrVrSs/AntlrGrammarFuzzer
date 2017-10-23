# Generated from mysqlParser.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .mysqlParser import mysqlParser
else:
    from mysqlParser import mysqlParser

# This class defines a complete listener for a parse tree produced by mysqlParser.
class mysqlParserListener(ParseTreeListener):

    # Enter a parse tree produced by mysqlParser#root.
    def enterRoot(self, ctx:mysqlParser.RootContext):
        pass

    # Exit a parse tree produced by mysqlParser#root.
    def exitRoot(self, ctx:mysqlParser.RootContext):
        pass


    # Enter a parse tree produced by mysqlParser#sqlStatements.
    def enterSqlStatements(self, ctx:mysqlParser.SqlStatementsContext):
        pass

    # Exit a parse tree produced by mysqlParser#sqlStatements.
    def exitSqlStatements(self, ctx:mysqlParser.SqlStatementsContext):
        pass


    # Enter a parse tree produced by mysqlParser#sqlStatement.
    def enterSqlStatement(self, ctx:mysqlParser.SqlStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#sqlStatement.
    def exitSqlStatement(self, ctx:mysqlParser.SqlStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#emptyStatement.
    def enterEmptyStatement(self, ctx:mysqlParser.EmptyStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#emptyStatement.
    def exitEmptyStatement(self, ctx:mysqlParser.EmptyStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#ddlStatement.
    def enterDdlStatement(self, ctx:mysqlParser.DdlStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#ddlStatement.
    def exitDdlStatement(self, ctx:mysqlParser.DdlStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#dmlStatement.
    def enterDmlStatement(self, ctx:mysqlParser.DmlStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#dmlStatement.
    def exitDmlStatement(self, ctx:mysqlParser.DmlStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#transactionStatement.
    def enterTransactionStatement(self, ctx:mysqlParser.TransactionStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#transactionStatement.
    def exitTransactionStatement(self, ctx:mysqlParser.TransactionStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#replicationStatement.
    def enterReplicationStatement(self, ctx:mysqlParser.ReplicationStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#replicationStatement.
    def exitReplicationStatement(self, ctx:mysqlParser.ReplicationStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#preparedStatement.
    def enterPreparedStatement(self, ctx:mysqlParser.PreparedStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#preparedStatement.
    def exitPreparedStatement(self, ctx:mysqlParser.PreparedStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#compoundStatement.
    def enterCompoundStatement(self, ctx:mysqlParser.CompoundStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#compoundStatement.
    def exitCompoundStatement(self, ctx:mysqlParser.CompoundStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#administrationStatement.
    def enterAdministrationStatement(self, ctx:mysqlParser.AdministrationStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#administrationStatement.
    def exitAdministrationStatement(self, ctx:mysqlParser.AdministrationStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#utilityStatement.
    def enterUtilityStatement(self, ctx:mysqlParser.UtilityStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#utilityStatement.
    def exitUtilityStatement(self, ctx:mysqlParser.UtilityStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#createDatabase.
    def enterCreateDatabase(self, ctx:mysqlParser.CreateDatabaseContext):
        pass

    # Exit a parse tree produced by mysqlParser#createDatabase.
    def exitCreateDatabase(self, ctx:mysqlParser.CreateDatabaseContext):
        pass


    # Enter a parse tree produced by mysqlParser#createEvent.
    def enterCreateEvent(self, ctx:mysqlParser.CreateEventContext):
        pass

    # Exit a parse tree produced by mysqlParser#createEvent.
    def exitCreateEvent(self, ctx:mysqlParser.CreateEventContext):
        pass


    # Enter a parse tree produced by mysqlParser#createIndex.
    def enterCreateIndex(self, ctx:mysqlParser.CreateIndexContext):
        pass

    # Exit a parse tree produced by mysqlParser#createIndex.
    def exitCreateIndex(self, ctx:mysqlParser.CreateIndexContext):
        pass


    # Enter a parse tree produced by mysqlParser#createLogfileGroup.
    def enterCreateLogfileGroup(self, ctx:mysqlParser.CreateLogfileGroupContext):
        pass

    # Exit a parse tree produced by mysqlParser#createLogfileGroup.
    def exitCreateLogfileGroup(self, ctx:mysqlParser.CreateLogfileGroupContext):
        pass


    # Enter a parse tree produced by mysqlParser#createProcedure.
    def enterCreateProcedure(self, ctx:mysqlParser.CreateProcedureContext):
        pass

    # Exit a parse tree produced by mysqlParser#createProcedure.
    def exitCreateProcedure(self, ctx:mysqlParser.CreateProcedureContext):
        pass


    # Enter a parse tree produced by mysqlParser#createFunction.
    def enterCreateFunction(self, ctx:mysqlParser.CreateFunctionContext):
        pass

    # Exit a parse tree produced by mysqlParser#createFunction.
    def exitCreateFunction(self, ctx:mysqlParser.CreateFunctionContext):
        pass


    # Enter a parse tree produced by mysqlParser#createServer.
    def enterCreateServer(self, ctx:mysqlParser.CreateServerContext):
        pass

    # Exit a parse tree produced by mysqlParser#createServer.
    def exitCreateServer(self, ctx:mysqlParser.CreateServerContext):
        pass


    # Enter a parse tree produced by mysqlParser#copyCreateTable.
    def enterCopyCreateTable(self, ctx:mysqlParser.CopyCreateTableContext):
        pass

    # Exit a parse tree produced by mysqlParser#copyCreateTable.
    def exitCopyCreateTable(self, ctx:mysqlParser.CopyCreateTableContext):
        pass


    # Enter a parse tree produced by mysqlParser#queryCreateTable.
    def enterQueryCreateTable(self, ctx:mysqlParser.QueryCreateTableContext):
        pass

    # Exit a parse tree produced by mysqlParser#queryCreateTable.
    def exitQueryCreateTable(self, ctx:mysqlParser.QueryCreateTableContext):
        pass


    # Enter a parse tree produced by mysqlParser#columnCreateTable.
    def enterColumnCreateTable(self, ctx:mysqlParser.ColumnCreateTableContext):
        pass

    # Exit a parse tree produced by mysqlParser#columnCreateTable.
    def exitColumnCreateTable(self, ctx:mysqlParser.ColumnCreateTableContext):
        pass


    # Enter a parse tree produced by mysqlParser#createTablespaceInnodb.
    def enterCreateTablespaceInnodb(self, ctx:mysqlParser.CreateTablespaceInnodbContext):
        pass

    # Exit a parse tree produced by mysqlParser#createTablespaceInnodb.
    def exitCreateTablespaceInnodb(self, ctx:mysqlParser.CreateTablespaceInnodbContext):
        pass


    # Enter a parse tree produced by mysqlParser#createTablespaceNdb.
    def enterCreateTablespaceNdb(self, ctx:mysqlParser.CreateTablespaceNdbContext):
        pass

    # Exit a parse tree produced by mysqlParser#createTablespaceNdb.
    def exitCreateTablespaceNdb(self, ctx:mysqlParser.CreateTablespaceNdbContext):
        pass


    # Enter a parse tree produced by mysqlParser#createTrigger.
    def enterCreateTrigger(self, ctx:mysqlParser.CreateTriggerContext):
        pass

    # Exit a parse tree produced by mysqlParser#createTrigger.
    def exitCreateTrigger(self, ctx:mysqlParser.CreateTriggerContext):
        pass


    # Enter a parse tree produced by mysqlParser#createView.
    def enterCreateView(self, ctx:mysqlParser.CreateViewContext):
        pass

    # Exit a parse tree produced by mysqlParser#createView.
    def exitCreateView(self, ctx:mysqlParser.CreateViewContext):
        pass


    # Enter a parse tree produced by mysqlParser#createDatabaseOption.
    def enterCreateDatabaseOption(self, ctx:mysqlParser.CreateDatabaseOptionContext):
        pass

    # Exit a parse tree produced by mysqlParser#createDatabaseOption.
    def exitCreateDatabaseOption(self, ctx:mysqlParser.CreateDatabaseOptionContext):
        pass


    # Enter a parse tree produced by mysqlParser#ownerStatement.
    def enterOwnerStatement(self, ctx:mysqlParser.OwnerStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#ownerStatement.
    def exitOwnerStatement(self, ctx:mysqlParser.OwnerStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#preciseSchedule.
    def enterPreciseSchedule(self, ctx:mysqlParser.PreciseScheduleContext):
        pass

    # Exit a parse tree produced by mysqlParser#preciseSchedule.
    def exitPreciseSchedule(self, ctx:mysqlParser.PreciseScheduleContext):
        pass


    # Enter a parse tree produced by mysqlParser#intervalSchedule.
    def enterIntervalSchedule(self, ctx:mysqlParser.IntervalScheduleContext):
        pass

    # Exit a parse tree produced by mysqlParser#intervalSchedule.
    def exitIntervalSchedule(self, ctx:mysqlParser.IntervalScheduleContext):
        pass


    # Enter a parse tree produced by mysqlParser#timestampValue.
    def enterTimestampValue(self, ctx:mysqlParser.TimestampValueContext):
        pass

    # Exit a parse tree produced by mysqlParser#timestampValue.
    def exitTimestampValue(self, ctx:mysqlParser.TimestampValueContext):
        pass


    # Enter a parse tree produced by mysqlParser#intervalExpr.
    def enterIntervalExpr(self, ctx:mysqlParser.IntervalExprContext):
        pass

    # Exit a parse tree produced by mysqlParser#intervalExpr.
    def exitIntervalExpr(self, ctx:mysqlParser.IntervalExprContext):
        pass


    # Enter a parse tree produced by mysqlParser#intervalType.
    def enterIntervalType(self, ctx:mysqlParser.IntervalTypeContext):
        pass

    # Exit a parse tree produced by mysqlParser#intervalType.
    def exitIntervalType(self, ctx:mysqlParser.IntervalTypeContext):
        pass


    # Enter a parse tree produced by mysqlParser#enableType.
    def enterEnableType(self, ctx:mysqlParser.EnableTypeContext):
        pass

    # Exit a parse tree produced by mysqlParser#enableType.
    def exitEnableType(self, ctx:mysqlParser.EnableTypeContext):
        pass


    # Enter a parse tree produced by mysqlParser#indexType.
    def enterIndexType(self, ctx:mysqlParser.IndexTypeContext):
        pass

    # Exit a parse tree produced by mysqlParser#indexType.
    def exitIndexType(self, ctx:mysqlParser.IndexTypeContext):
        pass


    # Enter a parse tree produced by mysqlParser#indexOption.
    def enterIndexOption(self, ctx:mysqlParser.IndexOptionContext):
        pass

    # Exit a parse tree produced by mysqlParser#indexOption.
    def exitIndexOption(self, ctx:mysqlParser.IndexOptionContext):
        pass


    # Enter a parse tree produced by mysqlParser#procedureParameter.
    def enterProcedureParameter(self, ctx:mysqlParser.ProcedureParameterContext):
        pass

    # Exit a parse tree produced by mysqlParser#procedureParameter.
    def exitProcedureParameter(self, ctx:mysqlParser.ProcedureParameterContext):
        pass


    # Enter a parse tree produced by mysqlParser#functionParameter.
    def enterFunctionParameter(self, ctx:mysqlParser.FunctionParameterContext):
        pass

    # Exit a parse tree produced by mysqlParser#functionParameter.
    def exitFunctionParameter(self, ctx:mysqlParser.FunctionParameterContext):
        pass


    # Enter a parse tree produced by mysqlParser#routineComment.
    def enterRoutineComment(self, ctx:mysqlParser.RoutineCommentContext):
        pass

    # Exit a parse tree produced by mysqlParser#routineComment.
    def exitRoutineComment(self, ctx:mysqlParser.RoutineCommentContext):
        pass


    # Enter a parse tree produced by mysqlParser#routineLanguage.
    def enterRoutineLanguage(self, ctx:mysqlParser.RoutineLanguageContext):
        pass

    # Exit a parse tree produced by mysqlParser#routineLanguage.
    def exitRoutineLanguage(self, ctx:mysqlParser.RoutineLanguageContext):
        pass


    # Enter a parse tree produced by mysqlParser#routineBehavior.
    def enterRoutineBehavior(self, ctx:mysqlParser.RoutineBehaviorContext):
        pass

    # Exit a parse tree produced by mysqlParser#routineBehavior.
    def exitRoutineBehavior(self, ctx:mysqlParser.RoutineBehaviorContext):
        pass


    # Enter a parse tree produced by mysqlParser#routineData.
    def enterRoutineData(self, ctx:mysqlParser.RoutineDataContext):
        pass

    # Exit a parse tree produced by mysqlParser#routineData.
    def exitRoutineData(self, ctx:mysqlParser.RoutineDataContext):
        pass


    # Enter a parse tree produced by mysqlParser#routineSecurity.
    def enterRoutineSecurity(self, ctx:mysqlParser.RoutineSecurityContext):
        pass

    # Exit a parse tree produced by mysqlParser#routineSecurity.
    def exitRoutineSecurity(self, ctx:mysqlParser.RoutineSecurityContext):
        pass


    # Enter a parse tree produced by mysqlParser#serverOption.
    def enterServerOption(self, ctx:mysqlParser.ServerOptionContext):
        pass

    # Exit a parse tree produced by mysqlParser#serverOption.
    def exitServerOption(self, ctx:mysqlParser.ServerOptionContext):
        pass


    # Enter a parse tree produced by mysqlParser#createDefinitions.
    def enterCreateDefinitions(self, ctx:mysqlParser.CreateDefinitionsContext):
        pass

    # Exit a parse tree produced by mysqlParser#createDefinitions.
    def exitCreateDefinitions(self, ctx:mysqlParser.CreateDefinitionsContext):
        pass


    # Enter a parse tree produced by mysqlParser#columnDeclaration.
    def enterColumnDeclaration(self, ctx:mysqlParser.ColumnDeclarationContext):
        pass

    # Exit a parse tree produced by mysqlParser#columnDeclaration.
    def exitColumnDeclaration(self, ctx:mysqlParser.ColumnDeclarationContext):
        pass


    # Enter a parse tree produced by mysqlParser#constraintDeclaration.
    def enterConstraintDeclaration(self, ctx:mysqlParser.ConstraintDeclarationContext):
        pass

    # Exit a parse tree produced by mysqlParser#constraintDeclaration.
    def exitConstraintDeclaration(self, ctx:mysqlParser.ConstraintDeclarationContext):
        pass


    # Enter a parse tree produced by mysqlParser#indexDeclaration.
    def enterIndexDeclaration(self, ctx:mysqlParser.IndexDeclarationContext):
        pass

    # Exit a parse tree produced by mysqlParser#indexDeclaration.
    def exitIndexDeclaration(self, ctx:mysqlParser.IndexDeclarationContext):
        pass


    # Enter a parse tree produced by mysqlParser#columnDefinition.
    def enterColumnDefinition(self, ctx:mysqlParser.ColumnDefinitionContext):
        pass

    # Exit a parse tree produced by mysqlParser#columnDefinition.
    def exitColumnDefinition(self, ctx:mysqlParser.ColumnDefinitionContext):
        pass


    # Enter a parse tree produced by mysqlParser#nullColumnConstraint.
    def enterNullColumnConstraint(self, ctx:mysqlParser.NullColumnConstraintContext):
        pass

    # Exit a parse tree produced by mysqlParser#nullColumnConstraint.
    def exitNullColumnConstraint(self, ctx:mysqlParser.NullColumnConstraintContext):
        pass


    # Enter a parse tree produced by mysqlParser#defaultColumnConstraint.
    def enterDefaultColumnConstraint(self, ctx:mysqlParser.DefaultColumnConstraintContext):
        pass

    # Exit a parse tree produced by mysqlParser#defaultColumnConstraint.
    def exitDefaultColumnConstraint(self, ctx:mysqlParser.DefaultColumnConstraintContext):
        pass


    # Enter a parse tree produced by mysqlParser#autoIncrementColumnConstraint.
    def enterAutoIncrementColumnConstraint(self, ctx:mysqlParser.AutoIncrementColumnConstraintContext):
        pass

    # Exit a parse tree produced by mysqlParser#autoIncrementColumnConstraint.
    def exitAutoIncrementColumnConstraint(self, ctx:mysqlParser.AutoIncrementColumnConstraintContext):
        pass


    # Enter a parse tree produced by mysqlParser#primaryKeyColumnConstraint.
    def enterPrimaryKeyColumnConstraint(self, ctx:mysqlParser.PrimaryKeyColumnConstraintContext):
        pass

    # Exit a parse tree produced by mysqlParser#primaryKeyColumnConstraint.
    def exitPrimaryKeyColumnConstraint(self, ctx:mysqlParser.PrimaryKeyColumnConstraintContext):
        pass


    # Enter a parse tree produced by mysqlParser#uniqueKeyColumnConstraint.
    def enterUniqueKeyColumnConstraint(self, ctx:mysqlParser.UniqueKeyColumnConstraintContext):
        pass

    # Exit a parse tree produced by mysqlParser#uniqueKeyColumnConstraint.
    def exitUniqueKeyColumnConstraint(self, ctx:mysqlParser.UniqueKeyColumnConstraintContext):
        pass


    # Enter a parse tree produced by mysqlParser#commentColumnConstraint.
    def enterCommentColumnConstraint(self, ctx:mysqlParser.CommentColumnConstraintContext):
        pass

    # Exit a parse tree produced by mysqlParser#commentColumnConstraint.
    def exitCommentColumnConstraint(self, ctx:mysqlParser.CommentColumnConstraintContext):
        pass


    # Enter a parse tree produced by mysqlParser#formatColumnConstraint.
    def enterFormatColumnConstraint(self, ctx:mysqlParser.FormatColumnConstraintContext):
        pass

    # Exit a parse tree produced by mysqlParser#formatColumnConstraint.
    def exitFormatColumnConstraint(self, ctx:mysqlParser.FormatColumnConstraintContext):
        pass


    # Enter a parse tree produced by mysqlParser#storageColumnConstraint.
    def enterStorageColumnConstraint(self, ctx:mysqlParser.StorageColumnConstraintContext):
        pass

    # Exit a parse tree produced by mysqlParser#storageColumnConstraint.
    def exitStorageColumnConstraint(self, ctx:mysqlParser.StorageColumnConstraintContext):
        pass


    # Enter a parse tree produced by mysqlParser#referenceColumnConstraint.
    def enterReferenceColumnConstraint(self, ctx:mysqlParser.ReferenceColumnConstraintContext):
        pass

    # Exit a parse tree produced by mysqlParser#referenceColumnConstraint.
    def exitReferenceColumnConstraint(self, ctx:mysqlParser.ReferenceColumnConstraintContext):
        pass


    # Enter a parse tree produced by mysqlParser#primaryKeyTableConstraint.
    def enterPrimaryKeyTableConstraint(self, ctx:mysqlParser.PrimaryKeyTableConstraintContext):
        pass

    # Exit a parse tree produced by mysqlParser#primaryKeyTableConstraint.
    def exitPrimaryKeyTableConstraint(self, ctx:mysqlParser.PrimaryKeyTableConstraintContext):
        pass


    # Enter a parse tree produced by mysqlParser#uniqueKeyTableConstraint.
    def enterUniqueKeyTableConstraint(self, ctx:mysqlParser.UniqueKeyTableConstraintContext):
        pass

    # Exit a parse tree produced by mysqlParser#uniqueKeyTableConstraint.
    def exitUniqueKeyTableConstraint(self, ctx:mysqlParser.UniqueKeyTableConstraintContext):
        pass


    # Enter a parse tree produced by mysqlParser#foreignKeyTableConstraint.
    def enterForeignKeyTableConstraint(self, ctx:mysqlParser.ForeignKeyTableConstraintContext):
        pass

    # Exit a parse tree produced by mysqlParser#foreignKeyTableConstraint.
    def exitForeignKeyTableConstraint(self, ctx:mysqlParser.ForeignKeyTableConstraintContext):
        pass


    # Enter a parse tree produced by mysqlParser#checkTableConstraint.
    def enterCheckTableConstraint(self, ctx:mysqlParser.CheckTableConstraintContext):
        pass

    # Exit a parse tree produced by mysqlParser#checkTableConstraint.
    def exitCheckTableConstraint(self, ctx:mysqlParser.CheckTableConstraintContext):
        pass


    # Enter a parse tree produced by mysqlParser#referenceDefinition.
    def enterReferenceDefinition(self, ctx:mysqlParser.ReferenceDefinitionContext):
        pass

    # Exit a parse tree produced by mysqlParser#referenceDefinition.
    def exitReferenceDefinition(self, ctx:mysqlParser.ReferenceDefinitionContext):
        pass


    # Enter a parse tree produced by mysqlParser#referenceAction.
    def enterReferenceAction(self, ctx:mysqlParser.ReferenceActionContext):
        pass

    # Exit a parse tree produced by mysqlParser#referenceAction.
    def exitReferenceAction(self, ctx:mysqlParser.ReferenceActionContext):
        pass


    # Enter a parse tree produced by mysqlParser#referenceControlType.
    def enterReferenceControlType(self, ctx:mysqlParser.ReferenceControlTypeContext):
        pass

    # Exit a parse tree produced by mysqlParser#referenceControlType.
    def exitReferenceControlType(self, ctx:mysqlParser.ReferenceControlTypeContext):
        pass


    # Enter a parse tree produced by mysqlParser#simpleIndexDeclaration.
    def enterSimpleIndexDeclaration(self, ctx:mysqlParser.SimpleIndexDeclarationContext):
        pass

    # Exit a parse tree produced by mysqlParser#simpleIndexDeclaration.
    def exitSimpleIndexDeclaration(self, ctx:mysqlParser.SimpleIndexDeclarationContext):
        pass


    # Enter a parse tree produced by mysqlParser#specialIndexDeclaration.
    def enterSpecialIndexDeclaration(self, ctx:mysqlParser.SpecialIndexDeclarationContext):
        pass

    # Exit a parse tree produced by mysqlParser#specialIndexDeclaration.
    def exitSpecialIndexDeclaration(self, ctx:mysqlParser.SpecialIndexDeclarationContext):
        pass


    # Enter a parse tree produced by mysqlParser#tableOptionEngine.
    def enterTableOptionEngine(self, ctx:mysqlParser.TableOptionEngineContext):
        pass

    # Exit a parse tree produced by mysqlParser#tableOptionEngine.
    def exitTableOptionEngine(self, ctx:mysqlParser.TableOptionEngineContext):
        pass


    # Enter a parse tree produced by mysqlParser#tableOptionAutoIncrement.
    def enterTableOptionAutoIncrement(self, ctx:mysqlParser.TableOptionAutoIncrementContext):
        pass

    # Exit a parse tree produced by mysqlParser#tableOptionAutoIncrement.
    def exitTableOptionAutoIncrement(self, ctx:mysqlParser.TableOptionAutoIncrementContext):
        pass


    # Enter a parse tree produced by mysqlParser#tableOptionAverage.
    def enterTableOptionAverage(self, ctx:mysqlParser.TableOptionAverageContext):
        pass

    # Exit a parse tree produced by mysqlParser#tableOptionAverage.
    def exitTableOptionAverage(self, ctx:mysqlParser.TableOptionAverageContext):
        pass


    # Enter a parse tree produced by mysqlParser#tableOptionCharset.
    def enterTableOptionCharset(self, ctx:mysqlParser.TableOptionCharsetContext):
        pass

    # Exit a parse tree produced by mysqlParser#tableOptionCharset.
    def exitTableOptionCharset(self, ctx:mysqlParser.TableOptionCharsetContext):
        pass


    # Enter a parse tree produced by mysqlParser#tableOptionChecksum.
    def enterTableOptionChecksum(self, ctx:mysqlParser.TableOptionChecksumContext):
        pass

    # Exit a parse tree produced by mysqlParser#tableOptionChecksum.
    def exitTableOptionChecksum(self, ctx:mysqlParser.TableOptionChecksumContext):
        pass


    # Enter a parse tree produced by mysqlParser#tableOptionCollate.
    def enterTableOptionCollate(self, ctx:mysqlParser.TableOptionCollateContext):
        pass

    # Exit a parse tree produced by mysqlParser#tableOptionCollate.
    def exitTableOptionCollate(self, ctx:mysqlParser.TableOptionCollateContext):
        pass


    # Enter a parse tree produced by mysqlParser#tableOptionComment.
    def enterTableOptionComment(self, ctx:mysqlParser.TableOptionCommentContext):
        pass

    # Exit a parse tree produced by mysqlParser#tableOptionComment.
    def exitTableOptionComment(self, ctx:mysqlParser.TableOptionCommentContext):
        pass


    # Enter a parse tree produced by mysqlParser#tableOptionCompression.
    def enterTableOptionCompression(self, ctx:mysqlParser.TableOptionCompressionContext):
        pass

    # Exit a parse tree produced by mysqlParser#tableOptionCompression.
    def exitTableOptionCompression(self, ctx:mysqlParser.TableOptionCompressionContext):
        pass


    # Enter a parse tree produced by mysqlParser#tableOptionConnection.
    def enterTableOptionConnection(self, ctx:mysqlParser.TableOptionConnectionContext):
        pass

    # Exit a parse tree produced by mysqlParser#tableOptionConnection.
    def exitTableOptionConnection(self, ctx:mysqlParser.TableOptionConnectionContext):
        pass


    # Enter a parse tree produced by mysqlParser#tableOptionDataDirectory.
    def enterTableOptionDataDirectory(self, ctx:mysqlParser.TableOptionDataDirectoryContext):
        pass

    # Exit a parse tree produced by mysqlParser#tableOptionDataDirectory.
    def exitTableOptionDataDirectory(self, ctx:mysqlParser.TableOptionDataDirectoryContext):
        pass


    # Enter a parse tree produced by mysqlParser#tableOptionDelay.
    def enterTableOptionDelay(self, ctx:mysqlParser.TableOptionDelayContext):
        pass

    # Exit a parse tree produced by mysqlParser#tableOptionDelay.
    def exitTableOptionDelay(self, ctx:mysqlParser.TableOptionDelayContext):
        pass


    # Enter a parse tree produced by mysqlParser#tableOptionEncryption.
    def enterTableOptionEncryption(self, ctx:mysqlParser.TableOptionEncryptionContext):
        pass

    # Exit a parse tree produced by mysqlParser#tableOptionEncryption.
    def exitTableOptionEncryption(self, ctx:mysqlParser.TableOptionEncryptionContext):
        pass


    # Enter a parse tree produced by mysqlParser#tableOptionIndexDirectory.
    def enterTableOptionIndexDirectory(self, ctx:mysqlParser.TableOptionIndexDirectoryContext):
        pass

    # Exit a parse tree produced by mysqlParser#tableOptionIndexDirectory.
    def exitTableOptionIndexDirectory(self, ctx:mysqlParser.TableOptionIndexDirectoryContext):
        pass


    # Enter a parse tree produced by mysqlParser#tableOptionInsertMethod.
    def enterTableOptionInsertMethod(self, ctx:mysqlParser.TableOptionInsertMethodContext):
        pass

    # Exit a parse tree produced by mysqlParser#tableOptionInsertMethod.
    def exitTableOptionInsertMethod(self, ctx:mysqlParser.TableOptionInsertMethodContext):
        pass


    # Enter a parse tree produced by mysqlParser#tableOptionKeyBlockSize.
    def enterTableOptionKeyBlockSize(self, ctx:mysqlParser.TableOptionKeyBlockSizeContext):
        pass

    # Exit a parse tree produced by mysqlParser#tableOptionKeyBlockSize.
    def exitTableOptionKeyBlockSize(self, ctx:mysqlParser.TableOptionKeyBlockSizeContext):
        pass


    # Enter a parse tree produced by mysqlParser#tableOptionMaxRows.
    def enterTableOptionMaxRows(self, ctx:mysqlParser.TableOptionMaxRowsContext):
        pass

    # Exit a parse tree produced by mysqlParser#tableOptionMaxRows.
    def exitTableOptionMaxRows(self, ctx:mysqlParser.TableOptionMaxRowsContext):
        pass


    # Enter a parse tree produced by mysqlParser#tableOptionMinRows.
    def enterTableOptionMinRows(self, ctx:mysqlParser.TableOptionMinRowsContext):
        pass

    # Exit a parse tree produced by mysqlParser#tableOptionMinRows.
    def exitTableOptionMinRows(self, ctx:mysqlParser.TableOptionMinRowsContext):
        pass


    # Enter a parse tree produced by mysqlParser#tableOptionPackKeys.
    def enterTableOptionPackKeys(self, ctx:mysqlParser.TableOptionPackKeysContext):
        pass

    # Exit a parse tree produced by mysqlParser#tableOptionPackKeys.
    def exitTableOptionPackKeys(self, ctx:mysqlParser.TableOptionPackKeysContext):
        pass


    # Enter a parse tree produced by mysqlParser#tableOptionPassword.
    def enterTableOptionPassword(self, ctx:mysqlParser.TableOptionPasswordContext):
        pass

    # Exit a parse tree produced by mysqlParser#tableOptionPassword.
    def exitTableOptionPassword(self, ctx:mysqlParser.TableOptionPasswordContext):
        pass


    # Enter a parse tree produced by mysqlParser#tableOptionRowFormat.
    def enterTableOptionRowFormat(self, ctx:mysqlParser.TableOptionRowFormatContext):
        pass

    # Exit a parse tree produced by mysqlParser#tableOptionRowFormat.
    def exitTableOptionRowFormat(self, ctx:mysqlParser.TableOptionRowFormatContext):
        pass


    # Enter a parse tree produced by mysqlParser#tableOptionRecalculation.
    def enterTableOptionRecalculation(self, ctx:mysqlParser.TableOptionRecalculationContext):
        pass

    # Exit a parse tree produced by mysqlParser#tableOptionRecalculation.
    def exitTableOptionRecalculation(self, ctx:mysqlParser.TableOptionRecalculationContext):
        pass


    # Enter a parse tree produced by mysqlParser#tableOptionPersistent.
    def enterTableOptionPersistent(self, ctx:mysqlParser.TableOptionPersistentContext):
        pass

    # Exit a parse tree produced by mysqlParser#tableOptionPersistent.
    def exitTableOptionPersistent(self, ctx:mysqlParser.TableOptionPersistentContext):
        pass


    # Enter a parse tree produced by mysqlParser#tableOptionSamplePage.
    def enterTableOptionSamplePage(self, ctx:mysqlParser.TableOptionSamplePageContext):
        pass

    # Exit a parse tree produced by mysqlParser#tableOptionSamplePage.
    def exitTableOptionSamplePage(self, ctx:mysqlParser.TableOptionSamplePageContext):
        pass


    # Enter a parse tree produced by mysqlParser#tableOptionTablespace.
    def enterTableOptionTablespace(self, ctx:mysqlParser.TableOptionTablespaceContext):
        pass

    # Exit a parse tree produced by mysqlParser#tableOptionTablespace.
    def exitTableOptionTablespace(self, ctx:mysqlParser.TableOptionTablespaceContext):
        pass


    # Enter a parse tree produced by mysqlParser#tableOptionUnion.
    def enterTableOptionUnion(self, ctx:mysqlParser.TableOptionUnionContext):
        pass

    # Exit a parse tree produced by mysqlParser#tableOptionUnion.
    def exitTableOptionUnion(self, ctx:mysqlParser.TableOptionUnionContext):
        pass


    # Enter a parse tree produced by mysqlParser#tablespaceStorage.
    def enterTablespaceStorage(self, ctx:mysqlParser.TablespaceStorageContext):
        pass

    # Exit a parse tree produced by mysqlParser#tablespaceStorage.
    def exitTablespaceStorage(self, ctx:mysqlParser.TablespaceStorageContext):
        pass


    # Enter a parse tree produced by mysqlParser#partitionDefinitions.
    def enterPartitionDefinitions(self, ctx:mysqlParser.PartitionDefinitionsContext):
        pass

    # Exit a parse tree produced by mysqlParser#partitionDefinitions.
    def exitPartitionDefinitions(self, ctx:mysqlParser.PartitionDefinitionsContext):
        pass


    # Enter a parse tree produced by mysqlParser#partitionFunctionHash.
    def enterPartitionFunctionHash(self, ctx:mysqlParser.PartitionFunctionHashContext):
        pass

    # Exit a parse tree produced by mysqlParser#partitionFunctionHash.
    def exitPartitionFunctionHash(self, ctx:mysqlParser.PartitionFunctionHashContext):
        pass


    # Enter a parse tree produced by mysqlParser#partitionFunctionKey.
    def enterPartitionFunctionKey(self, ctx:mysqlParser.PartitionFunctionKeyContext):
        pass

    # Exit a parse tree produced by mysqlParser#partitionFunctionKey.
    def exitPartitionFunctionKey(self, ctx:mysqlParser.PartitionFunctionKeyContext):
        pass


    # Enter a parse tree produced by mysqlParser#partitionFunctionRange.
    def enterPartitionFunctionRange(self, ctx:mysqlParser.PartitionFunctionRangeContext):
        pass

    # Exit a parse tree produced by mysqlParser#partitionFunctionRange.
    def exitPartitionFunctionRange(self, ctx:mysqlParser.PartitionFunctionRangeContext):
        pass


    # Enter a parse tree produced by mysqlParser#partitionFunctionList.
    def enterPartitionFunctionList(self, ctx:mysqlParser.PartitionFunctionListContext):
        pass

    # Exit a parse tree produced by mysqlParser#partitionFunctionList.
    def exitPartitionFunctionList(self, ctx:mysqlParser.PartitionFunctionListContext):
        pass


    # Enter a parse tree produced by mysqlParser#subPartitionFunctionHash.
    def enterSubPartitionFunctionHash(self, ctx:mysqlParser.SubPartitionFunctionHashContext):
        pass

    # Exit a parse tree produced by mysqlParser#subPartitionFunctionHash.
    def exitSubPartitionFunctionHash(self, ctx:mysqlParser.SubPartitionFunctionHashContext):
        pass


    # Enter a parse tree produced by mysqlParser#subPartitionFunctionKey.
    def enterSubPartitionFunctionKey(self, ctx:mysqlParser.SubPartitionFunctionKeyContext):
        pass

    # Exit a parse tree produced by mysqlParser#subPartitionFunctionKey.
    def exitSubPartitionFunctionKey(self, ctx:mysqlParser.SubPartitionFunctionKeyContext):
        pass


    # Enter a parse tree produced by mysqlParser#partitionComparision.
    def enterPartitionComparision(self, ctx:mysqlParser.PartitionComparisionContext):
        pass

    # Exit a parse tree produced by mysqlParser#partitionComparision.
    def exitPartitionComparision(self, ctx:mysqlParser.PartitionComparisionContext):
        pass


    # Enter a parse tree produced by mysqlParser#partitionList.
    def enterPartitionList(self, ctx:mysqlParser.PartitionListContext):
        pass

    # Exit a parse tree produced by mysqlParser#partitionList.
    def exitPartitionList(self, ctx:mysqlParser.PartitionListContext):
        pass


    # Enter a parse tree produced by mysqlParser#partitionSimple.
    def enterPartitionSimple(self, ctx:mysqlParser.PartitionSimpleContext):
        pass

    # Exit a parse tree produced by mysqlParser#partitionSimple.
    def exitPartitionSimple(self, ctx:mysqlParser.PartitionSimpleContext):
        pass


    # Enter a parse tree produced by mysqlParser#subpartitionDefinition.
    def enterSubpartitionDefinition(self, ctx:mysqlParser.SubpartitionDefinitionContext):
        pass

    # Exit a parse tree produced by mysqlParser#subpartitionDefinition.
    def exitSubpartitionDefinition(self, ctx:mysqlParser.SubpartitionDefinitionContext):
        pass


    # Enter a parse tree produced by mysqlParser#partitionOptionEngine.
    def enterPartitionOptionEngine(self, ctx:mysqlParser.PartitionOptionEngineContext):
        pass

    # Exit a parse tree produced by mysqlParser#partitionOptionEngine.
    def exitPartitionOptionEngine(self, ctx:mysqlParser.PartitionOptionEngineContext):
        pass


    # Enter a parse tree produced by mysqlParser#partitionOptionComment.
    def enterPartitionOptionComment(self, ctx:mysqlParser.PartitionOptionCommentContext):
        pass

    # Exit a parse tree produced by mysqlParser#partitionOptionComment.
    def exitPartitionOptionComment(self, ctx:mysqlParser.PartitionOptionCommentContext):
        pass


    # Enter a parse tree produced by mysqlParser#partitionOptionDataDirectory.
    def enterPartitionOptionDataDirectory(self, ctx:mysqlParser.PartitionOptionDataDirectoryContext):
        pass

    # Exit a parse tree produced by mysqlParser#partitionOptionDataDirectory.
    def exitPartitionOptionDataDirectory(self, ctx:mysqlParser.PartitionOptionDataDirectoryContext):
        pass


    # Enter a parse tree produced by mysqlParser#partitionOptionIndexDirectory.
    def enterPartitionOptionIndexDirectory(self, ctx:mysqlParser.PartitionOptionIndexDirectoryContext):
        pass

    # Exit a parse tree produced by mysqlParser#partitionOptionIndexDirectory.
    def exitPartitionOptionIndexDirectory(self, ctx:mysqlParser.PartitionOptionIndexDirectoryContext):
        pass


    # Enter a parse tree produced by mysqlParser#partitionOptionMaxRows.
    def enterPartitionOptionMaxRows(self, ctx:mysqlParser.PartitionOptionMaxRowsContext):
        pass

    # Exit a parse tree produced by mysqlParser#partitionOptionMaxRows.
    def exitPartitionOptionMaxRows(self, ctx:mysqlParser.PartitionOptionMaxRowsContext):
        pass


    # Enter a parse tree produced by mysqlParser#partitionOptionMinRows.
    def enterPartitionOptionMinRows(self, ctx:mysqlParser.PartitionOptionMinRowsContext):
        pass

    # Exit a parse tree produced by mysqlParser#partitionOptionMinRows.
    def exitPartitionOptionMinRows(self, ctx:mysqlParser.PartitionOptionMinRowsContext):
        pass


    # Enter a parse tree produced by mysqlParser#partitionOptionTablespace.
    def enterPartitionOptionTablespace(self, ctx:mysqlParser.PartitionOptionTablespaceContext):
        pass

    # Exit a parse tree produced by mysqlParser#partitionOptionTablespace.
    def exitPartitionOptionTablespace(self, ctx:mysqlParser.PartitionOptionTablespaceContext):
        pass


    # Enter a parse tree produced by mysqlParser#partitionOptionNodeGroup.
    def enterPartitionOptionNodeGroup(self, ctx:mysqlParser.PartitionOptionNodeGroupContext):
        pass

    # Exit a parse tree produced by mysqlParser#partitionOptionNodeGroup.
    def exitPartitionOptionNodeGroup(self, ctx:mysqlParser.PartitionOptionNodeGroupContext):
        pass


    # Enter a parse tree produced by mysqlParser#alterSimpleDatabase.
    def enterAlterSimpleDatabase(self, ctx:mysqlParser.AlterSimpleDatabaseContext):
        pass

    # Exit a parse tree produced by mysqlParser#alterSimpleDatabase.
    def exitAlterSimpleDatabase(self, ctx:mysqlParser.AlterSimpleDatabaseContext):
        pass


    # Enter a parse tree produced by mysqlParser#alterUpgradeName.
    def enterAlterUpgradeName(self, ctx:mysqlParser.AlterUpgradeNameContext):
        pass

    # Exit a parse tree produced by mysqlParser#alterUpgradeName.
    def exitAlterUpgradeName(self, ctx:mysqlParser.AlterUpgradeNameContext):
        pass


    # Enter a parse tree produced by mysqlParser#alterEvent.
    def enterAlterEvent(self, ctx:mysqlParser.AlterEventContext):
        pass

    # Exit a parse tree produced by mysqlParser#alterEvent.
    def exitAlterEvent(self, ctx:mysqlParser.AlterEventContext):
        pass


    # Enter a parse tree produced by mysqlParser#alterFunction.
    def enterAlterFunction(self, ctx:mysqlParser.AlterFunctionContext):
        pass

    # Exit a parse tree produced by mysqlParser#alterFunction.
    def exitAlterFunction(self, ctx:mysqlParser.AlterFunctionContext):
        pass


    # Enter a parse tree produced by mysqlParser#alterInstance.
    def enterAlterInstance(self, ctx:mysqlParser.AlterInstanceContext):
        pass

    # Exit a parse tree produced by mysqlParser#alterInstance.
    def exitAlterInstance(self, ctx:mysqlParser.AlterInstanceContext):
        pass


    # Enter a parse tree produced by mysqlParser#alterLogfileGroup.
    def enterAlterLogfileGroup(self, ctx:mysqlParser.AlterLogfileGroupContext):
        pass

    # Exit a parse tree produced by mysqlParser#alterLogfileGroup.
    def exitAlterLogfileGroup(self, ctx:mysqlParser.AlterLogfileGroupContext):
        pass


    # Enter a parse tree produced by mysqlParser#alterProcedure.
    def enterAlterProcedure(self, ctx:mysqlParser.AlterProcedureContext):
        pass

    # Exit a parse tree produced by mysqlParser#alterProcedure.
    def exitAlterProcedure(self, ctx:mysqlParser.AlterProcedureContext):
        pass


    # Enter a parse tree produced by mysqlParser#alterServer.
    def enterAlterServer(self, ctx:mysqlParser.AlterServerContext):
        pass

    # Exit a parse tree produced by mysqlParser#alterServer.
    def exitAlterServer(self, ctx:mysqlParser.AlterServerContext):
        pass


    # Enter a parse tree produced by mysqlParser#alterTable.
    def enterAlterTable(self, ctx:mysqlParser.AlterTableContext):
        pass

    # Exit a parse tree produced by mysqlParser#alterTable.
    def exitAlterTable(self, ctx:mysqlParser.AlterTableContext):
        pass


    # Enter a parse tree produced by mysqlParser#alterTablespace.
    def enterAlterTablespace(self, ctx:mysqlParser.AlterTablespaceContext):
        pass

    # Exit a parse tree produced by mysqlParser#alterTablespace.
    def exitAlterTablespace(self, ctx:mysqlParser.AlterTablespaceContext):
        pass


    # Enter a parse tree produced by mysqlParser#alterView.
    def enterAlterView(self, ctx:mysqlParser.AlterViewContext):
        pass

    # Exit a parse tree produced by mysqlParser#alterView.
    def exitAlterView(self, ctx:mysqlParser.AlterViewContext):
        pass


    # Enter a parse tree produced by mysqlParser#alterTableOption.
    def enterAlterTableOption(self, ctx:mysqlParser.AlterTableOptionContext):
        pass

    # Exit a parse tree produced by mysqlParser#alterTableOption.
    def exitAlterTableOption(self, ctx:mysqlParser.AlterTableOptionContext):
        pass


    # Enter a parse tree produced by mysqlParser#alterByAddColumn.
    def enterAlterByAddColumn(self, ctx:mysqlParser.AlterByAddColumnContext):
        pass

    # Exit a parse tree produced by mysqlParser#alterByAddColumn.
    def exitAlterByAddColumn(self, ctx:mysqlParser.AlterByAddColumnContext):
        pass


    # Enter a parse tree produced by mysqlParser#alterByAddColumns.
    def enterAlterByAddColumns(self, ctx:mysqlParser.AlterByAddColumnsContext):
        pass

    # Exit a parse tree produced by mysqlParser#alterByAddColumns.
    def exitAlterByAddColumns(self, ctx:mysqlParser.AlterByAddColumnsContext):
        pass


    # Enter a parse tree produced by mysqlParser#alterByAddIndex.
    def enterAlterByAddIndex(self, ctx:mysqlParser.AlterByAddIndexContext):
        pass

    # Exit a parse tree produced by mysqlParser#alterByAddIndex.
    def exitAlterByAddIndex(self, ctx:mysqlParser.AlterByAddIndexContext):
        pass


    # Enter a parse tree produced by mysqlParser#alterByAddPrimaryKey.
    def enterAlterByAddPrimaryKey(self, ctx:mysqlParser.AlterByAddPrimaryKeyContext):
        pass

    # Exit a parse tree produced by mysqlParser#alterByAddPrimaryKey.
    def exitAlterByAddPrimaryKey(self, ctx:mysqlParser.AlterByAddPrimaryKeyContext):
        pass


    # Enter a parse tree produced by mysqlParser#alterByAddUniqueKey.
    def enterAlterByAddUniqueKey(self, ctx:mysqlParser.AlterByAddUniqueKeyContext):
        pass

    # Exit a parse tree produced by mysqlParser#alterByAddUniqueKey.
    def exitAlterByAddUniqueKey(self, ctx:mysqlParser.AlterByAddUniqueKeyContext):
        pass


    # Enter a parse tree produced by mysqlParser#alterByAddSpecialIndex.
    def enterAlterByAddSpecialIndex(self, ctx:mysqlParser.AlterByAddSpecialIndexContext):
        pass

    # Exit a parse tree produced by mysqlParser#alterByAddSpecialIndex.
    def exitAlterByAddSpecialIndex(self, ctx:mysqlParser.AlterByAddSpecialIndexContext):
        pass


    # Enter a parse tree produced by mysqlParser#alterByAddForeignKey.
    def enterAlterByAddForeignKey(self, ctx:mysqlParser.AlterByAddForeignKeyContext):
        pass

    # Exit a parse tree produced by mysqlParser#alterByAddForeignKey.
    def exitAlterByAddForeignKey(self, ctx:mysqlParser.AlterByAddForeignKeyContext):
        pass


    # Enter a parse tree produced by mysqlParser#alterTableAlgorighm.
    def enterAlterTableAlgorighm(self, ctx:mysqlParser.AlterTableAlgorighmContext):
        pass

    # Exit a parse tree produced by mysqlParser#alterTableAlgorighm.
    def exitAlterTableAlgorighm(self, ctx:mysqlParser.AlterTableAlgorighmContext):
        pass


    # Enter a parse tree produced by mysqlParser#alterByChangeDefault.
    def enterAlterByChangeDefault(self, ctx:mysqlParser.AlterByChangeDefaultContext):
        pass

    # Exit a parse tree produced by mysqlParser#alterByChangeDefault.
    def exitAlterByChangeDefault(self, ctx:mysqlParser.AlterByChangeDefaultContext):
        pass


    # Enter a parse tree produced by mysqlParser#alterByChangeColumn.
    def enterAlterByChangeColumn(self, ctx:mysqlParser.AlterByChangeColumnContext):
        pass

    # Exit a parse tree produced by mysqlParser#alterByChangeColumn.
    def exitAlterByChangeColumn(self, ctx:mysqlParser.AlterByChangeColumnContext):
        pass


    # Enter a parse tree produced by mysqlParser#alterByLock.
    def enterAlterByLock(self, ctx:mysqlParser.AlterByLockContext):
        pass

    # Exit a parse tree produced by mysqlParser#alterByLock.
    def exitAlterByLock(self, ctx:mysqlParser.AlterByLockContext):
        pass


    # Enter a parse tree produced by mysqlParser#alterByModifyColumn.
    def enterAlterByModifyColumn(self, ctx:mysqlParser.AlterByModifyColumnContext):
        pass

    # Exit a parse tree produced by mysqlParser#alterByModifyColumn.
    def exitAlterByModifyColumn(self, ctx:mysqlParser.AlterByModifyColumnContext):
        pass


    # Enter a parse tree produced by mysqlParser#alterByDropColumn.
    def enterAlterByDropColumn(self, ctx:mysqlParser.AlterByDropColumnContext):
        pass

    # Exit a parse tree produced by mysqlParser#alterByDropColumn.
    def exitAlterByDropColumn(self, ctx:mysqlParser.AlterByDropColumnContext):
        pass


    # Enter a parse tree produced by mysqlParser#alterByDropPrimaryKey.
    def enterAlterByDropPrimaryKey(self, ctx:mysqlParser.AlterByDropPrimaryKeyContext):
        pass

    # Exit a parse tree produced by mysqlParser#alterByDropPrimaryKey.
    def exitAlterByDropPrimaryKey(self, ctx:mysqlParser.AlterByDropPrimaryKeyContext):
        pass


    # Enter a parse tree produced by mysqlParser#alterByDropIndex.
    def enterAlterByDropIndex(self, ctx:mysqlParser.AlterByDropIndexContext):
        pass

    # Exit a parse tree produced by mysqlParser#alterByDropIndex.
    def exitAlterByDropIndex(self, ctx:mysqlParser.AlterByDropIndexContext):
        pass


    # Enter a parse tree produced by mysqlParser#alterByDropForeignKey.
    def enterAlterByDropForeignKey(self, ctx:mysqlParser.AlterByDropForeignKeyContext):
        pass

    # Exit a parse tree produced by mysqlParser#alterByDropForeignKey.
    def exitAlterByDropForeignKey(self, ctx:mysqlParser.AlterByDropForeignKeyContext):
        pass


    # Enter a parse tree produced by mysqlParser#alterByDisableKeys.
    def enterAlterByDisableKeys(self, ctx:mysqlParser.AlterByDisableKeysContext):
        pass

    # Exit a parse tree produced by mysqlParser#alterByDisableKeys.
    def exitAlterByDisableKeys(self, ctx:mysqlParser.AlterByDisableKeysContext):
        pass


    # Enter a parse tree produced by mysqlParser#alterByEnableKeys.
    def enterAlterByEnableKeys(self, ctx:mysqlParser.AlterByEnableKeysContext):
        pass

    # Exit a parse tree produced by mysqlParser#alterByEnableKeys.
    def exitAlterByEnableKeys(self, ctx:mysqlParser.AlterByEnableKeysContext):
        pass


    # Enter a parse tree produced by mysqlParser#alterByRename.
    def enterAlterByRename(self, ctx:mysqlParser.AlterByRenameContext):
        pass

    # Exit a parse tree produced by mysqlParser#alterByRename.
    def exitAlterByRename(self, ctx:mysqlParser.AlterByRenameContext):
        pass


    # Enter a parse tree produced by mysqlParser#alterByOrder.
    def enterAlterByOrder(self, ctx:mysqlParser.AlterByOrderContext):
        pass

    # Exit a parse tree produced by mysqlParser#alterByOrder.
    def exitAlterByOrder(self, ctx:mysqlParser.AlterByOrderContext):
        pass


    # Enter a parse tree produced by mysqlParser#alterByConvertCharset.
    def enterAlterByConvertCharset(self, ctx:mysqlParser.AlterByConvertCharsetContext):
        pass

    # Exit a parse tree produced by mysqlParser#alterByConvertCharset.
    def exitAlterByConvertCharset(self, ctx:mysqlParser.AlterByConvertCharsetContext):
        pass


    # Enter a parse tree produced by mysqlParser#alterTableDefaultCharset.
    def enterAlterTableDefaultCharset(self, ctx:mysqlParser.AlterTableDefaultCharsetContext):
        pass

    # Exit a parse tree produced by mysqlParser#alterTableDefaultCharset.
    def exitAlterTableDefaultCharset(self, ctx:mysqlParser.AlterTableDefaultCharsetContext):
        pass


    # Enter a parse tree produced by mysqlParser#alterByDiscardTablespace.
    def enterAlterByDiscardTablespace(self, ctx:mysqlParser.AlterByDiscardTablespaceContext):
        pass

    # Exit a parse tree produced by mysqlParser#alterByDiscardTablespace.
    def exitAlterByDiscardTablespace(self, ctx:mysqlParser.AlterByDiscardTablespaceContext):
        pass


    # Enter a parse tree produced by mysqlParser#alterByImportTablespace.
    def enterAlterByImportTablespace(self, ctx:mysqlParser.AlterByImportTablespaceContext):
        pass

    # Exit a parse tree produced by mysqlParser#alterByImportTablespace.
    def exitAlterByImportTablespace(self, ctx:mysqlParser.AlterByImportTablespaceContext):
        pass


    # Enter a parse tree produced by mysqlParser#alterByForce.
    def enterAlterByForce(self, ctx:mysqlParser.AlterByForceContext):
        pass

    # Exit a parse tree produced by mysqlParser#alterByForce.
    def exitAlterByForce(self, ctx:mysqlParser.AlterByForceContext):
        pass


    # Enter a parse tree produced by mysqlParser#alterByValidate.
    def enterAlterByValidate(self, ctx:mysqlParser.AlterByValidateContext):
        pass

    # Exit a parse tree produced by mysqlParser#alterByValidate.
    def exitAlterByValidate(self, ctx:mysqlParser.AlterByValidateContext):
        pass


    # Enter a parse tree produced by mysqlParser#alterByAddPartition.
    def enterAlterByAddPartition(self, ctx:mysqlParser.AlterByAddPartitionContext):
        pass

    # Exit a parse tree produced by mysqlParser#alterByAddPartition.
    def exitAlterByAddPartition(self, ctx:mysqlParser.AlterByAddPartitionContext):
        pass


    # Enter a parse tree produced by mysqlParser#alterByDropPartition.
    def enterAlterByDropPartition(self, ctx:mysqlParser.AlterByDropPartitionContext):
        pass

    # Exit a parse tree produced by mysqlParser#alterByDropPartition.
    def exitAlterByDropPartition(self, ctx:mysqlParser.AlterByDropPartitionContext):
        pass


    # Enter a parse tree produced by mysqlParser#alterByDiscardPartition.
    def enterAlterByDiscardPartition(self, ctx:mysqlParser.AlterByDiscardPartitionContext):
        pass

    # Exit a parse tree produced by mysqlParser#alterByDiscardPartition.
    def exitAlterByDiscardPartition(self, ctx:mysqlParser.AlterByDiscardPartitionContext):
        pass


    # Enter a parse tree produced by mysqlParser#alterByImportPartition.
    def enterAlterByImportPartition(self, ctx:mysqlParser.AlterByImportPartitionContext):
        pass

    # Exit a parse tree produced by mysqlParser#alterByImportPartition.
    def exitAlterByImportPartition(self, ctx:mysqlParser.AlterByImportPartitionContext):
        pass


    # Enter a parse tree produced by mysqlParser#alterByTruncatePartition.
    def enterAlterByTruncatePartition(self, ctx:mysqlParser.AlterByTruncatePartitionContext):
        pass

    # Exit a parse tree produced by mysqlParser#alterByTruncatePartition.
    def exitAlterByTruncatePartition(self, ctx:mysqlParser.AlterByTruncatePartitionContext):
        pass


    # Enter a parse tree produced by mysqlParser#alterByCoalescePartition.
    def enterAlterByCoalescePartition(self, ctx:mysqlParser.AlterByCoalescePartitionContext):
        pass

    # Exit a parse tree produced by mysqlParser#alterByCoalescePartition.
    def exitAlterByCoalescePartition(self, ctx:mysqlParser.AlterByCoalescePartitionContext):
        pass


    # Enter a parse tree produced by mysqlParser#alterByReorganizePartition.
    def enterAlterByReorganizePartition(self, ctx:mysqlParser.AlterByReorganizePartitionContext):
        pass

    # Exit a parse tree produced by mysqlParser#alterByReorganizePartition.
    def exitAlterByReorganizePartition(self, ctx:mysqlParser.AlterByReorganizePartitionContext):
        pass


    # Enter a parse tree produced by mysqlParser#alterByExchangePartition.
    def enterAlterByExchangePartition(self, ctx:mysqlParser.AlterByExchangePartitionContext):
        pass

    # Exit a parse tree produced by mysqlParser#alterByExchangePartition.
    def exitAlterByExchangePartition(self, ctx:mysqlParser.AlterByExchangePartitionContext):
        pass


    # Enter a parse tree produced by mysqlParser#alterByAnalyzePartitiion.
    def enterAlterByAnalyzePartitiion(self, ctx:mysqlParser.AlterByAnalyzePartitiionContext):
        pass

    # Exit a parse tree produced by mysqlParser#alterByAnalyzePartitiion.
    def exitAlterByAnalyzePartitiion(self, ctx:mysqlParser.AlterByAnalyzePartitiionContext):
        pass


    # Enter a parse tree produced by mysqlParser#alterByCheckPartition.
    def enterAlterByCheckPartition(self, ctx:mysqlParser.AlterByCheckPartitionContext):
        pass

    # Exit a parse tree produced by mysqlParser#alterByCheckPartition.
    def exitAlterByCheckPartition(self, ctx:mysqlParser.AlterByCheckPartitionContext):
        pass


    # Enter a parse tree produced by mysqlParser#alterByOptimizePartition.
    def enterAlterByOptimizePartition(self, ctx:mysqlParser.AlterByOptimizePartitionContext):
        pass

    # Exit a parse tree produced by mysqlParser#alterByOptimizePartition.
    def exitAlterByOptimizePartition(self, ctx:mysqlParser.AlterByOptimizePartitionContext):
        pass


    # Enter a parse tree produced by mysqlParser#alterByRebuildPartition.
    def enterAlterByRebuildPartition(self, ctx:mysqlParser.AlterByRebuildPartitionContext):
        pass

    # Exit a parse tree produced by mysqlParser#alterByRebuildPartition.
    def exitAlterByRebuildPartition(self, ctx:mysqlParser.AlterByRebuildPartitionContext):
        pass


    # Enter a parse tree produced by mysqlParser#alterByRepairPartition.
    def enterAlterByRepairPartition(self, ctx:mysqlParser.AlterByRepairPartitionContext):
        pass

    # Exit a parse tree produced by mysqlParser#alterByRepairPartition.
    def exitAlterByRepairPartition(self, ctx:mysqlParser.AlterByRepairPartitionContext):
        pass


    # Enter a parse tree produced by mysqlParser#alterByRemovePartitioning.
    def enterAlterByRemovePartitioning(self, ctx:mysqlParser.AlterByRemovePartitioningContext):
        pass

    # Exit a parse tree produced by mysqlParser#alterByRemovePartitioning.
    def exitAlterByRemovePartitioning(self, ctx:mysqlParser.AlterByRemovePartitioningContext):
        pass


    # Enter a parse tree produced by mysqlParser#alterByUpgradePartitioning.
    def enterAlterByUpgradePartitioning(self, ctx:mysqlParser.AlterByUpgradePartitioningContext):
        pass

    # Exit a parse tree produced by mysqlParser#alterByUpgradePartitioning.
    def exitAlterByUpgradePartitioning(self, ctx:mysqlParser.AlterByUpgradePartitioningContext):
        pass


    # Enter a parse tree produced by mysqlParser#dropDatabase.
    def enterDropDatabase(self, ctx:mysqlParser.DropDatabaseContext):
        pass

    # Exit a parse tree produced by mysqlParser#dropDatabase.
    def exitDropDatabase(self, ctx:mysqlParser.DropDatabaseContext):
        pass


    # Enter a parse tree produced by mysqlParser#dropEvent.
    def enterDropEvent(self, ctx:mysqlParser.DropEventContext):
        pass

    # Exit a parse tree produced by mysqlParser#dropEvent.
    def exitDropEvent(self, ctx:mysqlParser.DropEventContext):
        pass


    # Enter a parse tree produced by mysqlParser#dropIndex.
    def enterDropIndex(self, ctx:mysqlParser.DropIndexContext):
        pass

    # Exit a parse tree produced by mysqlParser#dropIndex.
    def exitDropIndex(self, ctx:mysqlParser.DropIndexContext):
        pass


    # Enter a parse tree produced by mysqlParser#dropLogfileGroup.
    def enterDropLogfileGroup(self, ctx:mysqlParser.DropLogfileGroupContext):
        pass

    # Exit a parse tree produced by mysqlParser#dropLogfileGroup.
    def exitDropLogfileGroup(self, ctx:mysqlParser.DropLogfileGroupContext):
        pass


    # Enter a parse tree produced by mysqlParser#dropProcedure.
    def enterDropProcedure(self, ctx:mysqlParser.DropProcedureContext):
        pass

    # Exit a parse tree produced by mysqlParser#dropProcedure.
    def exitDropProcedure(self, ctx:mysqlParser.DropProcedureContext):
        pass


    # Enter a parse tree produced by mysqlParser#dropFunction.
    def enterDropFunction(self, ctx:mysqlParser.DropFunctionContext):
        pass

    # Exit a parse tree produced by mysqlParser#dropFunction.
    def exitDropFunction(self, ctx:mysqlParser.DropFunctionContext):
        pass


    # Enter a parse tree produced by mysqlParser#dropServer.
    def enterDropServer(self, ctx:mysqlParser.DropServerContext):
        pass

    # Exit a parse tree produced by mysqlParser#dropServer.
    def exitDropServer(self, ctx:mysqlParser.DropServerContext):
        pass


    # Enter a parse tree produced by mysqlParser#dropTable.
    def enterDropTable(self, ctx:mysqlParser.DropTableContext):
        pass

    # Exit a parse tree produced by mysqlParser#dropTable.
    def exitDropTable(self, ctx:mysqlParser.DropTableContext):
        pass


    # Enter a parse tree produced by mysqlParser#dropTablespace.
    def enterDropTablespace(self, ctx:mysqlParser.DropTablespaceContext):
        pass

    # Exit a parse tree produced by mysqlParser#dropTablespace.
    def exitDropTablespace(self, ctx:mysqlParser.DropTablespaceContext):
        pass


    # Enter a parse tree produced by mysqlParser#dropTrigger.
    def enterDropTrigger(self, ctx:mysqlParser.DropTriggerContext):
        pass

    # Exit a parse tree produced by mysqlParser#dropTrigger.
    def exitDropTrigger(self, ctx:mysqlParser.DropTriggerContext):
        pass


    # Enter a parse tree produced by mysqlParser#dropView.
    def enterDropView(self, ctx:mysqlParser.DropViewContext):
        pass

    # Exit a parse tree produced by mysqlParser#dropView.
    def exitDropView(self, ctx:mysqlParser.DropViewContext):
        pass


    # Enter a parse tree produced by mysqlParser#renameTable.
    def enterRenameTable(self, ctx:mysqlParser.RenameTableContext):
        pass

    # Exit a parse tree produced by mysqlParser#renameTable.
    def exitRenameTable(self, ctx:mysqlParser.RenameTableContext):
        pass


    # Enter a parse tree produced by mysqlParser#truncateTable.
    def enterTruncateTable(self, ctx:mysqlParser.TruncateTableContext):
        pass

    # Exit a parse tree produced by mysqlParser#truncateTable.
    def exitTruncateTable(self, ctx:mysqlParser.TruncateTableContext):
        pass


    # Enter a parse tree produced by mysqlParser#callStatement.
    def enterCallStatement(self, ctx:mysqlParser.CallStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#callStatement.
    def exitCallStatement(self, ctx:mysqlParser.CallStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#deleteStatement.
    def enterDeleteStatement(self, ctx:mysqlParser.DeleteStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#deleteStatement.
    def exitDeleteStatement(self, ctx:mysqlParser.DeleteStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#doStatement.
    def enterDoStatement(self, ctx:mysqlParser.DoStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#doStatement.
    def exitDoStatement(self, ctx:mysqlParser.DoStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#handlerStatement.
    def enterHandlerStatement(self, ctx:mysqlParser.HandlerStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#handlerStatement.
    def exitHandlerStatement(self, ctx:mysqlParser.HandlerStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#insertStatement.
    def enterInsertStatement(self, ctx:mysqlParser.InsertStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#insertStatement.
    def exitInsertStatement(self, ctx:mysqlParser.InsertStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#loadDataStatement.
    def enterLoadDataStatement(self, ctx:mysqlParser.LoadDataStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#loadDataStatement.
    def exitLoadDataStatement(self, ctx:mysqlParser.LoadDataStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#loadXmlStatement.
    def enterLoadXmlStatement(self, ctx:mysqlParser.LoadXmlStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#loadXmlStatement.
    def exitLoadXmlStatement(self, ctx:mysqlParser.LoadXmlStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#replaceStatement.
    def enterReplaceStatement(self, ctx:mysqlParser.ReplaceStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#replaceStatement.
    def exitReplaceStatement(self, ctx:mysqlParser.ReplaceStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#simpleSelect.
    def enterSimpleSelect(self, ctx:mysqlParser.SimpleSelectContext):
        pass

    # Exit a parse tree produced by mysqlParser#simpleSelect.
    def exitSimpleSelect(self, ctx:mysqlParser.SimpleSelectContext):
        pass


    # Enter a parse tree produced by mysqlParser#parenthesisSelect.
    def enterParenthesisSelect(self, ctx:mysqlParser.ParenthesisSelectContext):
        pass

    # Exit a parse tree produced by mysqlParser#parenthesisSelect.
    def exitParenthesisSelect(self, ctx:mysqlParser.ParenthesisSelectContext):
        pass


    # Enter a parse tree produced by mysqlParser#unionSelect.
    def enterUnionSelect(self, ctx:mysqlParser.UnionSelectContext):
        pass

    # Exit a parse tree produced by mysqlParser#unionSelect.
    def exitUnionSelect(self, ctx:mysqlParser.UnionSelectContext):
        pass


    # Enter a parse tree produced by mysqlParser#unionParenthesisSelect.
    def enterUnionParenthesisSelect(self, ctx:mysqlParser.UnionParenthesisSelectContext):
        pass

    # Exit a parse tree produced by mysqlParser#unionParenthesisSelect.
    def exitUnionParenthesisSelect(self, ctx:mysqlParser.UnionParenthesisSelectContext):
        pass


    # Enter a parse tree produced by mysqlParser#updateStatement.
    def enterUpdateStatement(self, ctx:mysqlParser.UpdateStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#updateStatement.
    def exitUpdateStatement(self, ctx:mysqlParser.UpdateStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#insertStatementValue.
    def enterInsertStatementValue(self, ctx:mysqlParser.InsertStatementValueContext):
        pass

    # Exit a parse tree produced by mysqlParser#insertStatementValue.
    def exitInsertStatementValue(self, ctx:mysqlParser.InsertStatementValueContext):
        pass


    # Enter a parse tree produced by mysqlParser#updatedElement.
    def enterUpdatedElement(self, ctx:mysqlParser.UpdatedElementContext):
        pass

    # Exit a parse tree produced by mysqlParser#updatedElement.
    def exitUpdatedElement(self, ctx:mysqlParser.UpdatedElementContext):
        pass


    # Enter a parse tree produced by mysqlParser#assignmentField.
    def enterAssignmentField(self, ctx:mysqlParser.AssignmentFieldContext):
        pass

    # Exit a parse tree produced by mysqlParser#assignmentField.
    def exitAssignmentField(self, ctx:mysqlParser.AssignmentFieldContext):
        pass


    # Enter a parse tree produced by mysqlParser#lockClause.
    def enterLockClause(self, ctx:mysqlParser.LockClauseContext):
        pass

    # Exit a parse tree produced by mysqlParser#lockClause.
    def exitLockClause(self, ctx:mysqlParser.LockClauseContext):
        pass


    # Enter a parse tree produced by mysqlParser#singleDeleteStatement.
    def enterSingleDeleteStatement(self, ctx:mysqlParser.SingleDeleteStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#singleDeleteStatement.
    def exitSingleDeleteStatement(self, ctx:mysqlParser.SingleDeleteStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#multipleDeleteStatement.
    def enterMultipleDeleteStatement(self, ctx:mysqlParser.MultipleDeleteStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#multipleDeleteStatement.
    def exitMultipleDeleteStatement(self, ctx:mysqlParser.MultipleDeleteStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#handlerOpenStatement.
    def enterHandlerOpenStatement(self, ctx:mysqlParser.HandlerOpenStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#handlerOpenStatement.
    def exitHandlerOpenStatement(self, ctx:mysqlParser.HandlerOpenStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#handlerReadIndexStatement.
    def enterHandlerReadIndexStatement(self, ctx:mysqlParser.HandlerReadIndexStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#handlerReadIndexStatement.
    def exitHandlerReadIndexStatement(self, ctx:mysqlParser.HandlerReadIndexStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#handlerReadStatement.
    def enterHandlerReadStatement(self, ctx:mysqlParser.HandlerReadStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#handlerReadStatement.
    def exitHandlerReadStatement(self, ctx:mysqlParser.HandlerReadStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#handlerCloseStatement.
    def enterHandlerCloseStatement(self, ctx:mysqlParser.HandlerCloseStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#handlerCloseStatement.
    def exitHandlerCloseStatement(self, ctx:mysqlParser.HandlerCloseStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#singleUpdateStatement.
    def enterSingleUpdateStatement(self, ctx:mysqlParser.SingleUpdateStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#singleUpdateStatement.
    def exitSingleUpdateStatement(self, ctx:mysqlParser.SingleUpdateStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#multipleUpdateStatement.
    def enterMultipleUpdateStatement(self, ctx:mysqlParser.MultipleUpdateStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#multipleUpdateStatement.
    def exitMultipleUpdateStatement(self, ctx:mysqlParser.MultipleUpdateStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#orderByClause.
    def enterOrderByClause(self, ctx:mysqlParser.OrderByClauseContext):
        pass

    # Exit a parse tree produced by mysqlParser#orderByClause.
    def exitOrderByClause(self, ctx:mysqlParser.OrderByClauseContext):
        pass


    # Enter a parse tree produced by mysqlParser#orderByExpression.
    def enterOrderByExpression(self, ctx:mysqlParser.OrderByExpressionContext):
        pass

    # Exit a parse tree produced by mysqlParser#orderByExpression.
    def exitOrderByExpression(self, ctx:mysqlParser.OrderByExpressionContext):
        pass


    # Enter a parse tree produced by mysqlParser#tableSources.
    def enterTableSources(self, ctx:mysqlParser.TableSourcesContext):
        pass

    # Exit a parse tree produced by mysqlParser#tableSources.
    def exitTableSources(self, ctx:mysqlParser.TableSourcesContext):
        pass


    # Enter a parse tree produced by mysqlParser#tableSource.
    def enterTableSource(self, ctx:mysqlParser.TableSourceContext):
        pass

    # Exit a parse tree produced by mysqlParser#tableSource.
    def exitTableSource(self, ctx:mysqlParser.TableSourceContext):
        pass


    # Enter a parse tree produced by mysqlParser#atomTableItem.
    def enterAtomTableItem(self, ctx:mysqlParser.AtomTableItemContext):
        pass

    # Exit a parse tree produced by mysqlParser#atomTableItem.
    def exitAtomTableItem(self, ctx:mysqlParser.AtomTableItemContext):
        pass


    # Enter a parse tree produced by mysqlParser#subqueryTableItem.
    def enterSubqueryTableItem(self, ctx:mysqlParser.SubqueryTableItemContext):
        pass

    # Exit a parse tree produced by mysqlParser#subqueryTableItem.
    def exitSubqueryTableItem(self, ctx:mysqlParser.SubqueryTableItemContext):
        pass


    # Enter a parse tree produced by mysqlParser#tableSourcesItem.
    def enterTableSourcesItem(self, ctx:mysqlParser.TableSourcesItemContext):
        pass

    # Exit a parse tree produced by mysqlParser#tableSourcesItem.
    def exitTableSourcesItem(self, ctx:mysqlParser.TableSourcesItemContext):
        pass


    # Enter a parse tree produced by mysqlParser#indexHint.
    def enterIndexHint(self, ctx:mysqlParser.IndexHintContext):
        pass

    # Exit a parse tree produced by mysqlParser#indexHint.
    def exitIndexHint(self, ctx:mysqlParser.IndexHintContext):
        pass


    # Enter a parse tree produced by mysqlParser#indexHintType.
    def enterIndexHintType(self, ctx:mysqlParser.IndexHintTypeContext):
        pass

    # Exit a parse tree produced by mysqlParser#indexHintType.
    def exitIndexHintType(self, ctx:mysqlParser.IndexHintTypeContext):
        pass


    # Enter a parse tree produced by mysqlParser#innerJoin.
    def enterInnerJoin(self, ctx:mysqlParser.InnerJoinContext):
        pass

    # Exit a parse tree produced by mysqlParser#innerJoin.
    def exitInnerJoin(self, ctx:mysqlParser.InnerJoinContext):
        pass


    # Enter a parse tree produced by mysqlParser#straightJoin.
    def enterStraightJoin(self, ctx:mysqlParser.StraightJoinContext):
        pass

    # Exit a parse tree produced by mysqlParser#straightJoin.
    def exitStraightJoin(self, ctx:mysqlParser.StraightJoinContext):
        pass


    # Enter a parse tree produced by mysqlParser#outerJoin.
    def enterOuterJoin(self, ctx:mysqlParser.OuterJoinContext):
        pass

    # Exit a parse tree produced by mysqlParser#outerJoin.
    def exitOuterJoin(self, ctx:mysqlParser.OuterJoinContext):
        pass


    # Enter a parse tree produced by mysqlParser#naturalJoin.
    def enterNaturalJoin(self, ctx:mysqlParser.NaturalJoinContext):
        pass

    # Exit a parse tree produced by mysqlParser#naturalJoin.
    def exitNaturalJoin(self, ctx:mysqlParser.NaturalJoinContext):
        pass


    # Enter a parse tree produced by mysqlParser#subquery.
    def enterSubquery(self, ctx:mysqlParser.SubqueryContext):
        pass

    # Exit a parse tree produced by mysqlParser#subquery.
    def exitSubquery(self, ctx:mysqlParser.SubqueryContext):
        pass


    # Enter a parse tree produced by mysqlParser#queryExpression.
    def enterQueryExpression(self, ctx:mysqlParser.QueryExpressionContext):
        pass

    # Exit a parse tree produced by mysqlParser#queryExpression.
    def exitQueryExpression(self, ctx:mysqlParser.QueryExpressionContext):
        pass


    # Enter a parse tree produced by mysqlParser#queryExpressionNointo.
    def enterQueryExpressionNointo(self, ctx:mysqlParser.QueryExpressionNointoContext):
        pass

    # Exit a parse tree produced by mysqlParser#queryExpressionNointo.
    def exitQueryExpressionNointo(self, ctx:mysqlParser.QueryExpressionNointoContext):
        pass


    # Enter a parse tree produced by mysqlParser#querySpecification.
    def enterQuerySpecification(self, ctx:mysqlParser.QuerySpecificationContext):
        pass

    # Exit a parse tree produced by mysqlParser#querySpecification.
    def exitQuerySpecification(self, ctx:mysqlParser.QuerySpecificationContext):
        pass


    # Enter a parse tree produced by mysqlParser#querySpecificationNointo.
    def enterQuerySpecificationNointo(self, ctx:mysqlParser.QuerySpecificationNointoContext):
        pass

    # Exit a parse tree produced by mysqlParser#querySpecificationNointo.
    def exitQuerySpecificationNointo(self, ctx:mysqlParser.QuerySpecificationNointoContext):
        pass


    # Enter a parse tree produced by mysqlParser#unionParenthesis.
    def enterUnionParenthesis(self, ctx:mysqlParser.UnionParenthesisContext):
        pass

    # Exit a parse tree produced by mysqlParser#unionParenthesis.
    def exitUnionParenthesis(self, ctx:mysqlParser.UnionParenthesisContext):
        pass


    # Enter a parse tree produced by mysqlParser#unionStatement.
    def enterUnionStatement(self, ctx:mysqlParser.UnionStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#unionStatement.
    def exitUnionStatement(self, ctx:mysqlParser.UnionStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#selectSpec.
    def enterSelectSpec(self, ctx:mysqlParser.SelectSpecContext):
        pass

    # Exit a parse tree produced by mysqlParser#selectSpec.
    def exitSelectSpec(self, ctx:mysqlParser.SelectSpecContext):
        pass


    # Enter a parse tree produced by mysqlParser#selectElements.
    def enterSelectElements(self, ctx:mysqlParser.SelectElementsContext):
        pass

    # Exit a parse tree produced by mysqlParser#selectElements.
    def exitSelectElements(self, ctx:mysqlParser.SelectElementsContext):
        pass


    # Enter a parse tree produced by mysqlParser#selectStarElement.
    def enterSelectStarElement(self, ctx:mysqlParser.SelectStarElementContext):
        pass

    # Exit a parse tree produced by mysqlParser#selectStarElement.
    def exitSelectStarElement(self, ctx:mysqlParser.SelectStarElementContext):
        pass


    # Enter a parse tree produced by mysqlParser#selectColumnElement.
    def enterSelectColumnElement(self, ctx:mysqlParser.SelectColumnElementContext):
        pass

    # Exit a parse tree produced by mysqlParser#selectColumnElement.
    def exitSelectColumnElement(self, ctx:mysqlParser.SelectColumnElementContext):
        pass


    # Enter a parse tree produced by mysqlParser#selectFunctionElement.
    def enterSelectFunctionElement(self, ctx:mysqlParser.SelectFunctionElementContext):
        pass

    # Exit a parse tree produced by mysqlParser#selectFunctionElement.
    def exitSelectFunctionElement(self, ctx:mysqlParser.SelectFunctionElementContext):
        pass


    # Enter a parse tree produced by mysqlParser#selectExpressionElement.
    def enterSelectExpressionElement(self, ctx:mysqlParser.SelectExpressionElementContext):
        pass

    # Exit a parse tree produced by mysqlParser#selectExpressionElement.
    def exitSelectExpressionElement(self, ctx:mysqlParser.SelectExpressionElementContext):
        pass


    # Enter a parse tree produced by mysqlParser#selectIntoVariables.
    def enterSelectIntoVariables(self, ctx:mysqlParser.SelectIntoVariablesContext):
        pass

    # Exit a parse tree produced by mysqlParser#selectIntoVariables.
    def exitSelectIntoVariables(self, ctx:mysqlParser.SelectIntoVariablesContext):
        pass


    # Enter a parse tree produced by mysqlParser#selectIntoDumpFile.
    def enterSelectIntoDumpFile(self, ctx:mysqlParser.SelectIntoDumpFileContext):
        pass

    # Exit a parse tree produced by mysqlParser#selectIntoDumpFile.
    def exitSelectIntoDumpFile(self, ctx:mysqlParser.SelectIntoDumpFileContext):
        pass


    # Enter a parse tree produced by mysqlParser#selectIntoTextFile.
    def enterSelectIntoTextFile(self, ctx:mysqlParser.SelectIntoTextFileContext):
        pass

    # Exit a parse tree produced by mysqlParser#selectIntoTextFile.
    def exitSelectIntoTextFile(self, ctx:mysqlParser.SelectIntoTextFileContext):
        pass


    # Enter a parse tree produced by mysqlParser#selectFieldsInto.
    def enterSelectFieldsInto(self, ctx:mysqlParser.SelectFieldsIntoContext):
        pass

    # Exit a parse tree produced by mysqlParser#selectFieldsInto.
    def exitSelectFieldsInto(self, ctx:mysqlParser.SelectFieldsIntoContext):
        pass


    # Enter a parse tree produced by mysqlParser#selectLinesInto.
    def enterSelectLinesInto(self, ctx:mysqlParser.SelectLinesIntoContext):
        pass

    # Exit a parse tree produced by mysqlParser#selectLinesInto.
    def exitSelectLinesInto(self, ctx:mysqlParser.SelectLinesIntoContext):
        pass


    # Enter a parse tree produced by mysqlParser#fromClause.
    def enterFromClause(self, ctx:mysqlParser.FromClauseContext):
        pass

    # Exit a parse tree produced by mysqlParser#fromClause.
    def exitFromClause(self, ctx:mysqlParser.FromClauseContext):
        pass


    # Enter a parse tree produced by mysqlParser#groupByItem.
    def enterGroupByItem(self, ctx:mysqlParser.GroupByItemContext):
        pass

    # Exit a parse tree produced by mysqlParser#groupByItem.
    def exitGroupByItem(self, ctx:mysqlParser.GroupByItemContext):
        pass


    # Enter a parse tree produced by mysqlParser#limitClause.
    def enterLimitClause(self, ctx:mysqlParser.LimitClauseContext):
        pass

    # Exit a parse tree produced by mysqlParser#limitClause.
    def exitLimitClause(self, ctx:mysqlParser.LimitClauseContext):
        pass


    # Enter a parse tree produced by mysqlParser#startTransaction.
    def enterStartTransaction(self, ctx:mysqlParser.StartTransactionContext):
        pass

    # Exit a parse tree produced by mysqlParser#startTransaction.
    def exitStartTransaction(self, ctx:mysqlParser.StartTransactionContext):
        pass


    # Enter a parse tree produced by mysqlParser#beginWork.
    def enterBeginWork(self, ctx:mysqlParser.BeginWorkContext):
        pass

    # Exit a parse tree produced by mysqlParser#beginWork.
    def exitBeginWork(self, ctx:mysqlParser.BeginWorkContext):
        pass


    # Enter a parse tree produced by mysqlParser#commitWork.
    def enterCommitWork(self, ctx:mysqlParser.CommitWorkContext):
        pass

    # Exit a parse tree produced by mysqlParser#commitWork.
    def exitCommitWork(self, ctx:mysqlParser.CommitWorkContext):
        pass


    # Enter a parse tree produced by mysqlParser#rollbackWork.
    def enterRollbackWork(self, ctx:mysqlParser.RollbackWorkContext):
        pass

    # Exit a parse tree produced by mysqlParser#rollbackWork.
    def exitRollbackWork(self, ctx:mysqlParser.RollbackWorkContext):
        pass


    # Enter a parse tree produced by mysqlParser#savepointStatement.
    def enterSavepointStatement(self, ctx:mysqlParser.SavepointStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#savepointStatement.
    def exitSavepointStatement(self, ctx:mysqlParser.SavepointStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#rollbackStatement.
    def enterRollbackStatement(self, ctx:mysqlParser.RollbackStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#rollbackStatement.
    def exitRollbackStatement(self, ctx:mysqlParser.RollbackStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#releaseStatement.
    def enterReleaseStatement(self, ctx:mysqlParser.ReleaseStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#releaseStatement.
    def exitReleaseStatement(self, ctx:mysqlParser.ReleaseStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#lockTables.
    def enterLockTables(self, ctx:mysqlParser.LockTablesContext):
        pass

    # Exit a parse tree produced by mysqlParser#lockTables.
    def exitLockTables(self, ctx:mysqlParser.LockTablesContext):
        pass


    # Enter a parse tree produced by mysqlParser#unlockTables.
    def enterUnlockTables(self, ctx:mysqlParser.UnlockTablesContext):
        pass

    # Exit a parse tree produced by mysqlParser#unlockTables.
    def exitUnlockTables(self, ctx:mysqlParser.UnlockTablesContext):
        pass


    # Enter a parse tree produced by mysqlParser#setAutocommitStatement.
    def enterSetAutocommitStatement(self, ctx:mysqlParser.SetAutocommitStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#setAutocommitStatement.
    def exitSetAutocommitStatement(self, ctx:mysqlParser.SetAutocommitStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#setTransactionStatement.
    def enterSetTransactionStatement(self, ctx:mysqlParser.SetTransactionStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#setTransactionStatement.
    def exitSetTransactionStatement(self, ctx:mysqlParser.SetTransactionStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#transactionMode.
    def enterTransactionMode(self, ctx:mysqlParser.TransactionModeContext):
        pass

    # Exit a parse tree produced by mysqlParser#transactionMode.
    def exitTransactionMode(self, ctx:mysqlParser.TransactionModeContext):
        pass


    # Enter a parse tree produced by mysqlParser#lockTableElement.
    def enterLockTableElement(self, ctx:mysqlParser.LockTableElementContext):
        pass

    # Exit a parse tree produced by mysqlParser#lockTableElement.
    def exitLockTableElement(self, ctx:mysqlParser.LockTableElementContext):
        pass


    # Enter a parse tree produced by mysqlParser#lockAction.
    def enterLockAction(self, ctx:mysqlParser.LockActionContext):
        pass

    # Exit a parse tree produced by mysqlParser#lockAction.
    def exitLockAction(self, ctx:mysqlParser.LockActionContext):
        pass


    # Enter a parse tree produced by mysqlParser#transactionOption.
    def enterTransactionOption(self, ctx:mysqlParser.TransactionOptionContext):
        pass

    # Exit a parse tree produced by mysqlParser#transactionOption.
    def exitTransactionOption(self, ctx:mysqlParser.TransactionOptionContext):
        pass


    # Enter a parse tree produced by mysqlParser#transactionLevel.
    def enterTransactionLevel(self, ctx:mysqlParser.TransactionLevelContext):
        pass

    # Exit a parse tree produced by mysqlParser#transactionLevel.
    def exitTransactionLevel(self, ctx:mysqlParser.TransactionLevelContext):
        pass


    # Enter a parse tree produced by mysqlParser#changeMaster.
    def enterChangeMaster(self, ctx:mysqlParser.ChangeMasterContext):
        pass

    # Exit a parse tree produced by mysqlParser#changeMaster.
    def exitChangeMaster(self, ctx:mysqlParser.ChangeMasterContext):
        pass


    # Enter a parse tree produced by mysqlParser#changeReplicationFilter.
    def enterChangeReplicationFilter(self, ctx:mysqlParser.ChangeReplicationFilterContext):
        pass

    # Exit a parse tree produced by mysqlParser#changeReplicationFilter.
    def exitChangeReplicationFilter(self, ctx:mysqlParser.ChangeReplicationFilterContext):
        pass


    # Enter a parse tree produced by mysqlParser#purgeBinaryLogs.
    def enterPurgeBinaryLogs(self, ctx:mysqlParser.PurgeBinaryLogsContext):
        pass

    # Exit a parse tree produced by mysqlParser#purgeBinaryLogs.
    def exitPurgeBinaryLogs(self, ctx:mysqlParser.PurgeBinaryLogsContext):
        pass


    # Enter a parse tree produced by mysqlParser#resetMaster.
    def enterResetMaster(self, ctx:mysqlParser.ResetMasterContext):
        pass

    # Exit a parse tree produced by mysqlParser#resetMaster.
    def exitResetMaster(self, ctx:mysqlParser.ResetMasterContext):
        pass


    # Enter a parse tree produced by mysqlParser#resetSlave.
    def enterResetSlave(self, ctx:mysqlParser.ResetSlaveContext):
        pass

    # Exit a parse tree produced by mysqlParser#resetSlave.
    def exitResetSlave(self, ctx:mysqlParser.ResetSlaveContext):
        pass


    # Enter a parse tree produced by mysqlParser#startSlave.
    def enterStartSlave(self, ctx:mysqlParser.StartSlaveContext):
        pass

    # Exit a parse tree produced by mysqlParser#startSlave.
    def exitStartSlave(self, ctx:mysqlParser.StartSlaveContext):
        pass


    # Enter a parse tree produced by mysqlParser#stopSlave.
    def enterStopSlave(self, ctx:mysqlParser.StopSlaveContext):
        pass

    # Exit a parse tree produced by mysqlParser#stopSlave.
    def exitStopSlave(self, ctx:mysqlParser.StopSlaveContext):
        pass


    # Enter a parse tree produced by mysqlParser#startGroupReplication.
    def enterStartGroupReplication(self, ctx:mysqlParser.StartGroupReplicationContext):
        pass

    # Exit a parse tree produced by mysqlParser#startGroupReplication.
    def exitStartGroupReplication(self, ctx:mysqlParser.StartGroupReplicationContext):
        pass


    # Enter a parse tree produced by mysqlParser#stopGroupReplication.
    def enterStopGroupReplication(self, ctx:mysqlParser.StopGroupReplicationContext):
        pass

    # Exit a parse tree produced by mysqlParser#stopGroupReplication.
    def exitStopGroupReplication(self, ctx:mysqlParser.StopGroupReplicationContext):
        pass


    # Enter a parse tree produced by mysqlParser#masterStringOption.
    def enterMasterStringOption(self, ctx:mysqlParser.MasterStringOptionContext):
        pass

    # Exit a parse tree produced by mysqlParser#masterStringOption.
    def exitMasterStringOption(self, ctx:mysqlParser.MasterStringOptionContext):
        pass


    # Enter a parse tree produced by mysqlParser#masterDecimalOption.
    def enterMasterDecimalOption(self, ctx:mysqlParser.MasterDecimalOptionContext):
        pass

    # Exit a parse tree produced by mysqlParser#masterDecimalOption.
    def exitMasterDecimalOption(self, ctx:mysqlParser.MasterDecimalOptionContext):
        pass


    # Enter a parse tree produced by mysqlParser#masterBoolOption.
    def enterMasterBoolOption(self, ctx:mysqlParser.MasterBoolOptionContext):
        pass

    # Exit a parse tree produced by mysqlParser#masterBoolOption.
    def exitMasterBoolOption(self, ctx:mysqlParser.MasterBoolOptionContext):
        pass


    # Enter a parse tree produced by mysqlParser#masterRealOption.
    def enterMasterRealOption(self, ctx:mysqlParser.MasterRealOptionContext):
        pass

    # Exit a parse tree produced by mysqlParser#masterRealOption.
    def exitMasterRealOption(self, ctx:mysqlParser.MasterRealOptionContext):
        pass


    # Enter a parse tree produced by mysqlParser#masterUidListOption.
    def enterMasterUidListOption(self, ctx:mysqlParser.MasterUidListOptionContext):
        pass

    # Exit a parse tree produced by mysqlParser#masterUidListOption.
    def exitMasterUidListOption(self, ctx:mysqlParser.MasterUidListOptionContext):
        pass


    # Enter a parse tree produced by mysqlParser#stringMasterOption.
    def enterStringMasterOption(self, ctx:mysqlParser.StringMasterOptionContext):
        pass

    # Exit a parse tree produced by mysqlParser#stringMasterOption.
    def exitStringMasterOption(self, ctx:mysqlParser.StringMasterOptionContext):
        pass


    # Enter a parse tree produced by mysqlParser#decimalMasterOption.
    def enterDecimalMasterOption(self, ctx:mysqlParser.DecimalMasterOptionContext):
        pass

    # Exit a parse tree produced by mysqlParser#decimalMasterOption.
    def exitDecimalMasterOption(self, ctx:mysqlParser.DecimalMasterOptionContext):
        pass


    # Enter a parse tree produced by mysqlParser#boolMasterOption.
    def enterBoolMasterOption(self, ctx:mysqlParser.BoolMasterOptionContext):
        pass

    # Exit a parse tree produced by mysqlParser#boolMasterOption.
    def exitBoolMasterOption(self, ctx:mysqlParser.BoolMasterOptionContext):
        pass


    # Enter a parse tree produced by mysqlParser#channelOption.
    def enterChannelOption(self, ctx:mysqlParser.ChannelOptionContext):
        pass

    # Exit a parse tree produced by mysqlParser#channelOption.
    def exitChannelOption(self, ctx:mysqlParser.ChannelOptionContext):
        pass


    # Enter a parse tree produced by mysqlParser#doDbReplication.
    def enterDoDbReplication(self, ctx:mysqlParser.DoDbReplicationContext):
        pass

    # Exit a parse tree produced by mysqlParser#doDbReplication.
    def exitDoDbReplication(self, ctx:mysqlParser.DoDbReplicationContext):
        pass


    # Enter a parse tree produced by mysqlParser#ignoreDbReplication.
    def enterIgnoreDbReplication(self, ctx:mysqlParser.IgnoreDbReplicationContext):
        pass

    # Exit a parse tree produced by mysqlParser#ignoreDbReplication.
    def exitIgnoreDbReplication(self, ctx:mysqlParser.IgnoreDbReplicationContext):
        pass


    # Enter a parse tree produced by mysqlParser#doTableReplication.
    def enterDoTableReplication(self, ctx:mysqlParser.DoTableReplicationContext):
        pass

    # Exit a parse tree produced by mysqlParser#doTableReplication.
    def exitDoTableReplication(self, ctx:mysqlParser.DoTableReplicationContext):
        pass


    # Enter a parse tree produced by mysqlParser#ignoreTableReplication.
    def enterIgnoreTableReplication(self, ctx:mysqlParser.IgnoreTableReplicationContext):
        pass

    # Exit a parse tree produced by mysqlParser#ignoreTableReplication.
    def exitIgnoreTableReplication(self, ctx:mysqlParser.IgnoreTableReplicationContext):
        pass


    # Enter a parse tree produced by mysqlParser#wildDoTableReplication.
    def enterWildDoTableReplication(self, ctx:mysqlParser.WildDoTableReplicationContext):
        pass

    # Exit a parse tree produced by mysqlParser#wildDoTableReplication.
    def exitWildDoTableReplication(self, ctx:mysqlParser.WildDoTableReplicationContext):
        pass


    # Enter a parse tree produced by mysqlParser#wildIgnoreTableReplication.
    def enterWildIgnoreTableReplication(self, ctx:mysqlParser.WildIgnoreTableReplicationContext):
        pass

    # Exit a parse tree produced by mysqlParser#wildIgnoreTableReplication.
    def exitWildIgnoreTableReplication(self, ctx:mysqlParser.WildIgnoreTableReplicationContext):
        pass


    # Enter a parse tree produced by mysqlParser#rewriteDbReplication.
    def enterRewriteDbReplication(self, ctx:mysqlParser.RewriteDbReplicationContext):
        pass

    # Exit a parse tree produced by mysqlParser#rewriteDbReplication.
    def exitRewriteDbReplication(self, ctx:mysqlParser.RewriteDbReplicationContext):
        pass


    # Enter a parse tree produced by mysqlParser#threadType.
    def enterThreadType(self, ctx:mysqlParser.ThreadTypeContext):
        pass

    # Exit a parse tree produced by mysqlParser#threadType.
    def exitThreadType(self, ctx:mysqlParser.ThreadTypeContext):
        pass


    # Enter a parse tree produced by mysqlParser#gtidsUntilOption.
    def enterGtidsUntilOption(self, ctx:mysqlParser.GtidsUntilOptionContext):
        pass

    # Exit a parse tree produced by mysqlParser#gtidsUntilOption.
    def exitGtidsUntilOption(self, ctx:mysqlParser.GtidsUntilOptionContext):
        pass


    # Enter a parse tree produced by mysqlParser#masterLogUntilOption.
    def enterMasterLogUntilOption(self, ctx:mysqlParser.MasterLogUntilOptionContext):
        pass

    # Exit a parse tree produced by mysqlParser#masterLogUntilOption.
    def exitMasterLogUntilOption(self, ctx:mysqlParser.MasterLogUntilOptionContext):
        pass


    # Enter a parse tree produced by mysqlParser#relayLogUntilOption.
    def enterRelayLogUntilOption(self, ctx:mysqlParser.RelayLogUntilOptionContext):
        pass

    # Exit a parse tree produced by mysqlParser#relayLogUntilOption.
    def exitRelayLogUntilOption(self, ctx:mysqlParser.RelayLogUntilOptionContext):
        pass


    # Enter a parse tree produced by mysqlParser#sqlGapsUntilOption.
    def enterSqlGapsUntilOption(self, ctx:mysqlParser.SqlGapsUntilOptionContext):
        pass

    # Exit a parse tree produced by mysqlParser#sqlGapsUntilOption.
    def exitSqlGapsUntilOption(self, ctx:mysqlParser.SqlGapsUntilOptionContext):
        pass


    # Enter a parse tree produced by mysqlParser#connectionOption.
    def enterConnectionOption(self, ctx:mysqlParser.ConnectionOptionContext):
        pass

    # Exit a parse tree produced by mysqlParser#connectionOption.
    def exitConnectionOption(self, ctx:mysqlParser.ConnectionOptionContext):
        pass


    # Enter a parse tree produced by mysqlParser#gtuidSet.
    def enterGtuidSet(self, ctx:mysqlParser.GtuidSetContext):
        pass

    # Exit a parse tree produced by mysqlParser#gtuidSet.
    def exitGtuidSet(self, ctx:mysqlParser.GtuidSetContext):
        pass


    # Enter a parse tree produced by mysqlParser#xaStartTransaction.
    def enterXaStartTransaction(self, ctx:mysqlParser.XaStartTransactionContext):
        pass

    # Exit a parse tree produced by mysqlParser#xaStartTransaction.
    def exitXaStartTransaction(self, ctx:mysqlParser.XaStartTransactionContext):
        pass


    # Enter a parse tree produced by mysqlParser#xaEndTransaction.
    def enterXaEndTransaction(self, ctx:mysqlParser.XaEndTransactionContext):
        pass

    # Exit a parse tree produced by mysqlParser#xaEndTransaction.
    def exitXaEndTransaction(self, ctx:mysqlParser.XaEndTransactionContext):
        pass


    # Enter a parse tree produced by mysqlParser#xaPrepareStatement.
    def enterXaPrepareStatement(self, ctx:mysqlParser.XaPrepareStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#xaPrepareStatement.
    def exitXaPrepareStatement(self, ctx:mysqlParser.XaPrepareStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#xaCommitWork.
    def enterXaCommitWork(self, ctx:mysqlParser.XaCommitWorkContext):
        pass

    # Exit a parse tree produced by mysqlParser#xaCommitWork.
    def exitXaCommitWork(self, ctx:mysqlParser.XaCommitWorkContext):
        pass


    # Enter a parse tree produced by mysqlParser#xaRollbackWork.
    def enterXaRollbackWork(self, ctx:mysqlParser.XaRollbackWorkContext):
        pass

    # Exit a parse tree produced by mysqlParser#xaRollbackWork.
    def exitXaRollbackWork(self, ctx:mysqlParser.XaRollbackWorkContext):
        pass


    # Enter a parse tree produced by mysqlParser#xaRecoverWork.
    def enterXaRecoverWork(self, ctx:mysqlParser.XaRecoverWorkContext):
        pass

    # Exit a parse tree produced by mysqlParser#xaRecoverWork.
    def exitXaRecoverWork(self, ctx:mysqlParser.XaRecoverWorkContext):
        pass


    # Enter a parse tree produced by mysqlParser#prepareStatement.
    def enterPrepareStatement(self, ctx:mysqlParser.PrepareStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#prepareStatement.
    def exitPrepareStatement(self, ctx:mysqlParser.PrepareStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#executeStatement.
    def enterExecuteStatement(self, ctx:mysqlParser.ExecuteStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#executeStatement.
    def exitExecuteStatement(self, ctx:mysqlParser.ExecuteStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#deallocatePrepare.
    def enterDeallocatePrepare(self, ctx:mysqlParser.DeallocatePrepareContext):
        pass

    # Exit a parse tree produced by mysqlParser#deallocatePrepare.
    def exitDeallocatePrepare(self, ctx:mysqlParser.DeallocatePrepareContext):
        pass


    # Enter a parse tree produced by mysqlParser#routineBody.
    def enterRoutineBody(self, ctx:mysqlParser.RoutineBodyContext):
        pass

    # Exit a parse tree produced by mysqlParser#routineBody.
    def exitRoutineBody(self, ctx:mysqlParser.RoutineBodyContext):
        pass


    # Enter a parse tree produced by mysqlParser#blockStatement.
    def enterBlockStatement(self, ctx:mysqlParser.BlockStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#blockStatement.
    def exitBlockStatement(self, ctx:mysqlParser.BlockStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#caseStatement.
    def enterCaseStatement(self, ctx:mysqlParser.CaseStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#caseStatement.
    def exitCaseStatement(self, ctx:mysqlParser.CaseStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#ifStatement.
    def enterIfStatement(self, ctx:mysqlParser.IfStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#ifStatement.
    def exitIfStatement(self, ctx:mysqlParser.IfStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#iterateStatement.
    def enterIterateStatement(self, ctx:mysqlParser.IterateStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#iterateStatement.
    def exitIterateStatement(self, ctx:mysqlParser.IterateStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#leaveStatement.
    def enterLeaveStatement(self, ctx:mysqlParser.LeaveStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#leaveStatement.
    def exitLeaveStatement(self, ctx:mysqlParser.LeaveStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#loopStatement.
    def enterLoopStatement(self, ctx:mysqlParser.LoopStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#loopStatement.
    def exitLoopStatement(self, ctx:mysqlParser.LoopStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#repeatStatement.
    def enterRepeatStatement(self, ctx:mysqlParser.RepeatStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#repeatStatement.
    def exitRepeatStatement(self, ctx:mysqlParser.RepeatStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#returnStatement.
    def enterReturnStatement(self, ctx:mysqlParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#returnStatement.
    def exitReturnStatement(self, ctx:mysqlParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#whileStatement.
    def enterWhileStatement(self, ctx:mysqlParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#whileStatement.
    def exitWhileStatement(self, ctx:mysqlParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#CloseCursor.
    def enterCloseCursor(self, ctx:mysqlParser.CloseCursorContext):
        pass

    # Exit a parse tree produced by mysqlParser#CloseCursor.
    def exitCloseCursor(self, ctx:mysqlParser.CloseCursorContext):
        pass


    # Enter a parse tree produced by mysqlParser#FetchCursor.
    def enterFetchCursor(self, ctx:mysqlParser.FetchCursorContext):
        pass

    # Exit a parse tree produced by mysqlParser#FetchCursor.
    def exitFetchCursor(self, ctx:mysqlParser.FetchCursorContext):
        pass


    # Enter a parse tree produced by mysqlParser#OpenCursor.
    def enterOpenCursor(self, ctx:mysqlParser.OpenCursorContext):
        pass

    # Exit a parse tree produced by mysqlParser#OpenCursor.
    def exitOpenCursor(self, ctx:mysqlParser.OpenCursorContext):
        pass


    # Enter a parse tree produced by mysqlParser#declareVariable.
    def enterDeclareVariable(self, ctx:mysqlParser.DeclareVariableContext):
        pass

    # Exit a parse tree produced by mysqlParser#declareVariable.
    def exitDeclareVariable(self, ctx:mysqlParser.DeclareVariableContext):
        pass


    # Enter a parse tree produced by mysqlParser#declareCondition.
    def enterDeclareCondition(self, ctx:mysqlParser.DeclareConditionContext):
        pass

    # Exit a parse tree produced by mysqlParser#declareCondition.
    def exitDeclareCondition(self, ctx:mysqlParser.DeclareConditionContext):
        pass


    # Enter a parse tree produced by mysqlParser#declareCursor.
    def enterDeclareCursor(self, ctx:mysqlParser.DeclareCursorContext):
        pass

    # Exit a parse tree produced by mysqlParser#declareCursor.
    def exitDeclareCursor(self, ctx:mysqlParser.DeclareCursorContext):
        pass


    # Enter a parse tree produced by mysqlParser#declareHandler.
    def enterDeclareHandler(self, ctx:mysqlParser.DeclareHandlerContext):
        pass

    # Exit a parse tree produced by mysqlParser#declareHandler.
    def exitDeclareHandler(self, ctx:mysqlParser.DeclareHandlerContext):
        pass


    # Enter a parse tree produced by mysqlParser#handlerConditionValue.
    def enterHandlerConditionValue(self, ctx:mysqlParser.HandlerConditionValueContext):
        pass

    # Exit a parse tree produced by mysqlParser#handlerConditionValue.
    def exitHandlerConditionValue(self, ctx:mysqlParser.HandlerConditionValueContext):
        pass


    # Enter a parse tree produced by mysqlParser#procedureSqlStatement.
    def enterProcedureSqlStatement(self, ctx:mysqlParser.ProcedureSqlStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#procedureSqlStatement.
    def exitProcedureSqlStatement(self, ctx:mysqlParser.ProcedureSqlStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#caseAlternative.
    def enterCaseAlternative(self, ctx:mysqlParser.CaseAlternativeContext):
        pass

    # Exit a parse tree produced by mysqlParser#caseAlternative.
    def exitCaseAlternative(self, ctx:mysqlParser.CaseAlternativeContext):
        pass


    # Enter a parse tree produced by mysqlParser#elifAlternative.
    def enterElifAlternative(self, ctx:mysqlParser.ElifAlternativeContext):
        pass

    # Exit a parse tree produced by mysqlParser#elifAlternative.
    def exitElifAlternative(self, ctx:mysqlParser.ElifAlternativeContext):
        pass


    # Enter a parse tree produced by mysqlParser#alterUserMysqlV56.
    def enterAlterUserMysqlV56(self, ctx:mysqlParser.AlterUserMysqlV56Context):
        pass

    # Exit a parse tree produced by mysqlParser#alterUserMysqlV56.
    def exitAlterUserMysqlV56(self, ctx:mysqlParser.AlterUserMysqlV56Context):
        pass


    # Enter a parse tree produced by mysqlParser#alterUserMysqlV57.
    def enterAlterUserMysqlV57(self, ctx:mysqlParser.AlterUserMysqlV57Context):
        pass

    # Exit a parse tree produced by mysqlParser#alterUserMysqlV57.
    def exitAlterUserMysqlV57(self, ctx:mysqlParser.AlterUserMysqlV57Context):
        pass


    # Enter a parse tree produced by mysqlParser#createUserMysqlV56.
    def enterCreateUserMysqlV56(self, ctx:mysqlParser.CreateUserMysqlV56Context):
        pass

    # Exit a parse tree produced by mysqlParser#createUserMysqlV56.
    def exitCreateUserMysqlV56(self, ctx:mysqlParser.CreateUserMysqlV56Context):
        pass


    # Enter a parse tree produced by mysqlParser#createUserMysqlV57.
    def enterCreateUserMysqlV57(self, ctx:mysqlParser.CreateUserMysqlV57Context):
        pass

    # Exit a parse tree produced by mysqlParser#createUserMysqlV57.
    def exitCreateUserMysqlV57(self, ctx:mysqlParser.CreateUserMysqlV57Context):
        pass


    # Enter a parse tree produced by mysqlParser#dropUser.
    def enterDropUser(self, ctx:mysqlParser.DropUserContext):
        pass

    # Exit a parse tree produced by mysqlParser#dropUser.
    def exitDropUser(self, ctx:mysqlParser.DropUserContext):
        pass


    # Enter a parse tree produced by mysqlParser#grantStatement.
    def enterGrantStatement(self, ctx:mysqlParser.GrantStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#grantStatement.
    def exitGrantStatement(self, ctx:mysqlParser.GrantStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#grantProxy.
    def enterGrantProxy(self, ctx:mysqlParser.GrantProxyContext):
        pass

    # Exit a parse tree produced by mysqlParser#grantProxy.
    def exitGrantProxy(self, ctx:mysqlParser.GrantProxyContext):
        pass


    # Enter a parse tree produced by mysqlParser#renameUser.
    def enterRenameUser(self, ctx:mysqlParser.RenameUserContext):
        pass

    # Exit a parse tree produced by mysqlParser#renameUser.
    def exitRenameUser(self, ctx:mysqlParser.RenameUserContext):
        pass


    # Enter a parse tree produced by mysqlParser#detailRevoke.
    def enterDetailRevoke(self, ctx:mysqlParser.DetailRevokeContext):
        pass

    # Exit a parse tree produced by mysqlParser#detailRevoke.
    def exitDetailRevoke(self, ctx:mysqlParser.DetailRevokeContext):
        pass


    # Enter a parse tree produced by mysqlParser#shortRevoke.
    def enterShortRevoke(self, ctx:mysqlParser.ShortRevokeContext):
        pass

    # Exit a parse tree produced by mysqlParser#shortRevoke.
    def exitShortRevoke(self, ctx:mysqlParser.ShortRevokeContext):
        pass


    # Enter a parse tree produced by mysqlParser#revokeProxy.
    def enterRevokeProxy(self, ctx:mysqlParser.RevokeProxyContext):
        pass

    # Exit a parse tree produced by mysqlParser#revokeProxy.
    def exitRevokeProxy(self, ctx:mysqlParser.RevokeProxyContext):
        pass


    # Enter a parse tree produced by mysqlParser#setPasswordStatement.
    def enterSetPasswordStatement(self, ctx:mysqlParser.SetPasswordStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#setPasswordStatement.
    def exitSetPasswordStatement(self, ctx:mysqlParser.SetPasswordStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#userPasswordOption.
    def enterUserPasswordOption(self, ctx:mysqlParser.UserPasswordOptionContext):
        pass

    # Exit a parse tree produced by mysqlParser#userPasswordOption.
    def exitUserPasswordOption(self, ctx:mysqlParser.UserPasswordOptionContext):
        pass


    # Enter a parse tree produced by mysqlParser#passwordAuthOption.
    def enterPasswordAuthOption(self, ctx:mysqlParser.PasswordAuthOptionContext):
        pass

    # Exit a parse tree produced by mysqlParser#passwordAuthOption.
    def exitPasswordAuthOption(self, ctx:mysqlParser.PasswordAuthOptionContext):
        pass


    # Enter a parse tree produced by mysqlParser#stringAuthOption.
    def enterStringAuthOption(self, ctx:mysqlParser.StringAuthOptionContext):
        pass

    # Exit a parse tree produced by mysqlParser#stringAuthOption.
    def exitStringAuthOption(self, ctx:mysqlParser.StringAuthOptionContext):
        pass


    # Enter a parse tree produced by mysqlParser#hashAuthOption.
    def enterHashAuthOption(self, ctx:mysqlParser.HashAuthOptionContext):
        pass

    # Exit a parse tree produced by mysqlParser#hashAuthOption.
    def exitHashAuthOption(self, ctx:mysqlParser.HashAuthOptionContext):
        pass


    # Enter a parse tree produced by mysqlParser#tlsOption.
    def enterTlsOption(self, ctx:mysqlParser.TlsOptionContext):
        pass

    # Exit a parse tree produced by mysqlParser#tlsOption.
    def exitTlsOption(self, ctx:mysqlParser.TlsOptionContext):
        pass


    # Enter a parse tree produced by mysqlParser#userResourceOption.
    def enterUserResourceOption(self, ctx:mysqlParser.UserResourceOptionContext):
        pass

    # Exit a parse tree produced by mysqlParser#userResourceOption.
    def exitUserResourceOption(self, ctx:mysqlParser.UserResourceOptionContext):
        pass


    # Enter a parse tree produced by mysqlParser#userLockOption.
    def enterUserLockOption(self, ctx:mysqlParser.UserLockOptionContext):
        pass

    # Exit a parse tree produced by mysqlParser#userLockOption.
    def exitUserLockOption(self, ctx:mysqlParser.UserLockOptionContext):
        pass


    # Enter a parse tree produced by mysqlParser#privelegeClause.
    def enterPrivelegeClause(self, ctx:mysqlParser.PrivelegeClauseContext):
        pass

    # Exit a parse tree produced by mysqlParser#privelegeClause.
    def exitPrivelegeClause(self, ctx:mysqlParser.PrivelegeClauseContext):
        pass


    # Enter a parse tree produced by mysqlParser#privilege.
    def enterPrivilege(self, ctx:mysqlParser.PrivilegeContext):
        pass

    # Exit a parse tree produced by mysqlParser#privilege.
    def exitPrivilege(self, ctx:mysqlParser.PrivilegeContext):
        pass


    # Enter a parse tree produced by mysqlParser#privilegeLevel.
    def enterPrivilegeLevel(self, ctx:mysqlParser.PrivilegeLevelContext):
        pass

    # Exit a parse tree produced by mysqlParser#privilegeLevel.
    def exitPrivilegeLevel(self, ctx:mysqlParser.PrivilegeLevelContext):
        pass


    # Enter a parse tree produced by mysqlParser#analyzeTable.
    def enterAnalyzeTable(self, ctx:mysqlParser.AnalyzeTableContext):
        pass

    # Exit a parse tree produced by mysqlParser#analyzeTable.
    def exitAnalyzeTable(self, ctx:mysqlParser.AnalyzeTableContext):
        pass


    # Enter a parse tree produced by mysqlParser#checkTable.
    def enterCheckTable(self, ctx:mysqlParser.CheckTableContext):
        pass

    # Exit a parse tree produced by mysqlParser#checkTable.
    def exitCheckTable(self, ctx:mysqlParser.CheckTableContext):
        pass


    # Enter a parse tree produced by mysqlParser#checksumTable.
    def enterChecksumTable(self, ctx:mysqlParser.ChecksumTableContext):
        pass

    # Exit a parse tree produced by mysqlParser#checksumTable.
    def exitChecksumTable(self, ctx:mysqlParser.ChecksumTableContext):
        pass


    # Enter a parse tree produced by mysqlParser#optimizeTable.
    def enterOptimizeTable(self, ctx:mysqlParser.OptimizeTableContext):
        pass

    # Exit a parse tree produced by mysqlParser#optimizeTable.
    def exitOptimizeTable(self, ctx:mysqlParser.OptimizeTableContext):
        pass


    # Enter a parse tree produced by mysqlParser#repairTable.
    def enterRepairTable(self, ctx:mysqlParser.RepairTableContext):
        pass

    # Exit a parse tree produced by mysqlParser#repairTable.
    def exitRepairTable(self, ctx:mysqlParser.RepairTableContext):
        pass


    # Enter a parse tree produced by mysqlParser#checkTableOption.
    def enterCheckTableOption(self, ctx:mysqlParser.CheckTableOptionContext):
        pass

    # Exit a parse tree produced by mysqlParser#checkTableOption.
    def exitCheckTableOption(self, ctx:mysqlParser.CheckTableOptionContext):
        pass


    # Enter a parse tree produced by mysqlParser#createUdfunction.
    def enterCreateUdfunction(self, ctx:mysqlParser.CreateUdfunctionContext):
        pass

    # Exit a parse tree produced by mysqlParser#createUdfunction.
    def exitCreateUdfunction(self, ctx:mysqlParser.CreateUdfunctionContext):
        pass


    # Enter a parse tree produced by mysqlParser#installPlugin.
    def enterInstallPlugin(self, ctx:mysqlParser.InstallPluginContext):
        pass

    # Exit a parse tree produced by mysqlParser#installPlugin.
    def exitInstallPlugin(self, ctx:mysqlParser.InstallPluginContext):
        pass


    # Enter a parse tree produced by mysqlParser#uninstallPlugin.
    def enterUninstallPlugin(self, ctx:mysqlParser.UninstallPluginContext):
        pass

    # Exit a parse tree produced by mysqlParser#uninstallPlugin.
    def exitUninstallPlugin(self, ctx:mysqlParser.UninstallPluginContext):
        pass


    # Enter a parse tree produced by mysqlParser#setVariable.
    def enterSetVariable(self, ctx:mysqlParser.SetVariableContext):
        pass

    # Exit a parse tree produced by mysqlParser#setVariable.
    def exitSetVariable(self, ctx:mysqlParser.SetVariableContext):
        pass


    # Enter a parse tree produced by mysqlParser#setCharset.
    def enterSetCharset(self, ctx:mysqlParser.SetCharsetContext):
        pass

    # Exit a parse tree produced by mysqlParser#setCharset.
    def exitSetCharset(self, ctx:mysqlParser.SetCharsetContext):
        pass


    # Enter a parse tree produced by mysqlParser#setNames.
    def enterSetNames(self, ctx:mysqlParser.SetNamesContext):
        pass

    # Exit a parse tree produced by mysqlParser#setNames.
    def exitSetNames(self, ctx:mysqlParser.SetNamesContext):
        pass


    # Enter a parse tree produced by mysqlParser#setPassword.
    def enterSetPassword(self, ctx:mysqlParser.SetPasswordContext):
        pass

    # Exit a parse tree produced by mysqlParser#setPassword.
    def exitSetPassword(self, ctx:mysqlParser.SetPasswordContext):
        pass


    # Enter a parse tree produced by mysqlParser#setTransaction.
    def enterSetTransaction(self, ctx:mysqlParser.SetTransactionContext):
        pass

    # Exit a parse tree produced by mysqlParser#setTransaction.
    def exitSetTransaction(self, ctx:mysqlParser.SetTransactionContext):
        pass


    # Enter a parse tree produced by mysqlParser#setAutocommit.
    def enterSetAutocommit(self, ctx:mysqlParser.SetAutocommitContext):
        pass

    # Exit a parse tree produced by mysqlParser#setAutocommit.
    def exitSetAutocommit(self, ctx:mysqlParser.SetAutocommitContext):
        pass


    # Enter a parse tree produced by mysqlParser#showMasterLogs.
    def enterShowMasterLogs(self, ctx:mysqlParser.ShowMasterLogsContext):
        pass

    # Exit a parse tree produced by mysqlParser#showMasterLogs.
    def exitShowMasterLogs(self, ctx:mysqlParser.ShowMasterLogsContext):
        pass


    # Enter a parse tree produced by mysqlParser#showLogEvents.
    def enterShowLogEvents(self, ctx:mysqlParser.ShowLogEventsContext):
        pass

    # Exit a parse tree produced by mysqlParser#showLogEvents.
    def exitShowLogEvents(self, ctx:mysqlParser.ShowLogEventsContext):
        pass


    # Enter a parse tree produced by mysqlParser#showObjectFilter.
    def enterShowObjectFilter(self, ctx:mysqlParser.ShowObjectFilterContext):
        pass

    # Exit a parse tree produced by mysqlParser#showObjectFilter.
    def exitShowObjectFilter(self, ctx:mysqlParser.ShowObjectFilterContext):
        pass


    # Enter a parse tree produced by mysqlParser#showColumns.
    def enterShowColumns(self, ctx:mysqlParser.ShowColumnsContext):
        pass

    # Exit a parse tree produced by mysqlParser#showColumns.
    def exitShowColumns(self, ctx:mysqlParser.ShowColumnsContext):
        pass


    # Enter a parse tree produced by mysqlParser#showCreateDb.
    def enterShowCreateDb(self, ctx:mysqlParser.ShowCreateDbContext):
        pass

    # Exit a parse tree produced by mysqlParser#showCreateDb.
    def exitShowCreateDb(self, ctx:mysqlParser.ShowCreateDbContext):
        pass


    # Enter a parse tree produced by mysqlParser#showCreateFullIdObject.
    def enterShowCreateFullIdObject(self, ctx:mysqlParser.ShowCreateFullIdObjectContext):
        pass

    # Exit a parse tree produced by mysqlParser#showCreateFullIdObject.
    def exitShowCreateFullIdObject(self, ctx:mysqlParser.ShowCreateFullIdObjectContext):
        pass


    # Enter a parse tree produced by mysqlParser#showCreateUser.
    def enterShowCreateUser(self, ctx:mysqlParser.ShowCreateUserContext):
        pass

    # Exit a parse tree produced by mysqlParser#showCreateUser.
    def exitShowCreateUser(self, ctx:mysqlParser.ShowCreateUserContext):
        pass


    # Enter a parse tree produced by mysqlParser#showEngine.
    def enterShowEngine(self, ctx:mysqlParser.ShowEngineContext):
        pass

    # Exit a parse tree produced by mysqlParser#showEngine.
    def exitShowEngine(self, ctx:mysqlParser.ShowEngineContext):
        pass


    # Enter a parse tree produced by mysqlParser#showGlobalInfo.
    def enterShowGlobalInfo(self, ctx:mysqlParser.ShowGlobalInfoContext):
        pass

    # Exit a parse tree produced by mysqlParser#showGlobalInfo.
    def exitShowGlobalInfo(self, ctx:mysqlParser.ShowGlobalInfoContext):
        pass


    # Enter a parse tree produced by mysqlParser#showErrors.
    def enterShowErrors(self, ctx:mysqlParser.ShowErrorsContext):
        pass

    # Exit a parse tree produced by mysqlParser#showErrors.
    def exitShowErrors(self, ctx:mysqlParser.ShowErrorsContext):
        pass


    # Enter a parse tree produced by mysqlParser#showCountErrors.
    def enterShowCountErrors(self, ctx:mysqlParser.ShowCountErrorsContext):
        pass

    # Exit a parse tree produced by mysqlParser#showCountErrors.
    def exitShowCountErrors(self, ctx:mysqlParser.ShowCountErrorsContext):
        pass


    # Enter a parse tree produced by mysqlParser#showSchemaFilter.
    def enterShowSchemaFilter(self, ctx:mysqlParser.ShowSchemaFilterContext):
        pass

    # Exit a parse tree produced by mysqlParser#showSchemaFilter.
    def exitShowSchemaFilter(self, ctx:mysqlParser.ShowSchemaFilterContext):
        pass


    # Enter a parse tree produced by mysqlParser#showRoutine.
    def enterShowRoutine(self, ctx:mysqlParser.ShowRoutineContext):
        pass

    # Exit a parse tree produced by mysqlParser#showRoutine.
    def exitShowRoutine(self, ctx:mysqlParser.ShowRoutineContext):
        pass


    # Enter a parse tree produced by mysqlParser#showGrants.
    def enterShowGrants(self, ctx:mysqlParser.ShowGrantsContext):
        pass

    # Exit a parse tree produced by mysqlParser#showGrants.
    def exitShowGrants(self, ctx:mysqlParser.ShowGrantsContext):
        pass


    # Enter a parse tree produced by mysqlParser#showIndexes.
    def enterShowIndexes(self, ctx:mysqlParser.ShowIndexesContext):
        pass

    # Exit a parse tree produced by mysqlParser#showIndexes.
    def exitShowIndexes(self, ctx:mysqlParser.ShowIndexesContext):
        pass


    # Enter a parse tree produced by mysqlParser#showOpenTables.
    def enterShowOpenTables(self, ctx:mysqlParser.ShowOpenTablesContext):
        pass

    # Exit a parse tree produced by mysqlParser#showOpenTables.
    def exitShowOpenTables(self, ctx:mysqlParser.ShowOpenTablesContext):
        pass


    # Enter a parse tree produced by mysqlParser#showProfile.
    def enterShowProfile(self, ctx:mysqlParser.ShowProfileContext):
        pass

    # Exit a parse tree produced by mysqlParser#showProfile.
    def exitShowProfile(self, ctx:mysqlParser.ShowProfileContext):
        pass


    # Enter a parse tree produced by mysqlParser#showSlaveStatus.
    def enterShowSlaveStatus(self, ctx:mysqlParser.ShowSlaveStatusContext):
        pass

    # Exit a parse tree produced by mysqlParser#showSlaveStatus.
    def exitShowSlaveStatus(self, ctx:mysqlParser.ShowSlaveStatusContext):
        pass


    # Enter a parse tree produced by mysqlParser#variableClause.
    def enterVariableClause(self, ctx:mysqlParser.VariableClauseContext):
        pass

    # Exit a parse tree produced by mysqlParser#variableClause.
    def exitVariableClause(self, ctx:mysqlParser.VariableClauseContext):
        pass


    # Enter a parse tree produced by mysqlParser#showCommonEntity.
    def enterShowCommonEntity(self, ctx:mysqlParser.ShowCommonEntityContext):
        pass

    # Exit a parse tree produced by mysqlParser#showCommonEntity.
    def exitShowCommonEntity(self, ctx:mysqlParser.ShowCommonEntityContext):
        pass


    # Enter a parse tree produced by mysqlParser#showFilter.
    def enterShowFilter(self, ctx:mysqlParser.ShowFilterContext):
        pass

    # Exit a parse tree produced by mysqlParser#showFilter.
    def exitShowFilter(self, ctx:mysqlParser.ShowFilterContext):
        pass


    # Enter a parse tree produced by mysqlParser#showGlobalInfoClause.
    def enterShowGlobalInfoClause(self, ctx:mysqlParser.ShowGlobalInfoClauseContext):
        pass

    # Exit a parse tree produced by mysqlParser#showGlobalInfoClause.
    def exitShowGlobalInfoClause(self, ctx:mysqlParser.ShowGlobalInfoClauseContext):
        pass


    # Enter a parse tree produced by mysqlParser#showSchemaEntity.
    def enterShowSchemaEntity(self, ctx:mysqlParser.ShowSchemaEntityContext):
        pass

    # Exit a parse tree produced by mysqlParser#showSchemaEntity.
    def exitShowSchemaEntity(self, ctx:mysqlParser.ShowSchemaEntityContext):
        pass


    # Enter a parse tree produced by mysqlParser#showProfileType.
    def enterShowProfileType(self, ctx:mysqlParser.ShowProfileTypeContext):
        pass

    # Exit a parse tree produced by mysqlParser#showProfileType.
    def exitShowProfileType(self, ctx:mysqlParser.ShowProfileTypeContext):
        pass


    # Enter a parse tree produced by mysqlParser#binlogStatement.
    def enterBinlogStatement(self, ctx:mysqlParser.BinlogStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#binlogStatement.
    def exitBinlogStatement(self, ctx:mysqlParser.BinlogStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#cacheIndexStatement.
    def enterCacheIndexStatement(self, ctx:mysqlParser.CacheIndexStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#cacheIndexStatement.
    def exitCacheIndexStatement(self, ctx:mysqlParser.CacheIndexStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#flushStatement.
    def enterFlushStatement(self, ctx:mysqlParser.FlushStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#flushStatement.
    def exitFlushStatement(self, ctx:mysqlParser.FlushStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#killStatement.
    def enterKillStatement(self, ctx:mysqlParser.KillStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#killStatement.
    def exitKillStatement(self, ctx:mysqlParser.KillStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#loadIndexIntoCache.
    def enterLoadIndexIntoCache(self, ctx:mysqlParser.LoadIndexIntoCacheContext):
        pass

    # Exit a parse tree produced by mysqlParser#loadIndexIntoCache.
    def exitLoadIndexIntoCache(self, ctx:mysqlParser.LoadIndexIntoCacheContext):
        pass


    # Enter a parse tree produced by mysqlParser#resetStatement.
    def enterResetStatement(self, ctx:mysqlParser.ResetStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#resetStatement.
    def exitResetStatement(self, ctx:mysqlParser.ResetStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#shutdownStatement.
    def enterShutdownStatement(self, ctx:mysqlParser.ShutdownStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#shutdownStatement.
    def exitShutdownStatement(self, ctx:mysqlParser.ShutdownStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#tableIndexes.
    def enterTableIndexes(self, ctx:mysqlParser.TableIndexesContext):
        pass

    # Exit a parse tree produced by mysqlParser#tableIndexes.
    def exitTableIndexes(self, ctx:mysqlParser.TableIndexesContext):
        pass


    # Enter a parse tree produced by mysqlParser#simpleFlushOption.
    def enterSimpleFlushOption(self, ctx:mysqlParser.SimpleFlushOptionContext):
        pass

    # Exit a parse tree produced by mysqlParser#simpleFlushOption.
    def exitSimpleFlushOption(self, ctx:mysqlParser.SimpleFlushOptionContext):
        pass


    # Enter a parse tree produced by mysqlParser#channelFlushOption.
    def enterChannelFlushOption(self, ctx:mysqlParser.ChannelFlushOptionContext):
        pass

    # Exit a parse tree produced by mysqlParser#channelFlushOption.
    def exitChannelFlushOption(self, ctx:mysqlParser.ChannelFlushOptionContext):
        pass


    # Enter a parse tree produced by mysqlParser#tableFlushOption.
    def enterTableFlushOption(self, ctx:mysqlParser.TableFlushOptionContext):
        pass

    # Exit a parse tree produced by mysqlParser#tableFlushOption.
    def exitTableFlushOption(self, ctx:mysqlParser.TableFlushOptionContext):
        pass


    # Enter a parse tree produced by mysqlParser#loadedTableIndexes.
    def enterLoadedTableIndexes(self, ctx:mysqlParser.LoadedTableIndexesContext):
        pass

    # Exit a parse tree produced by mysqlParser#loadedTableIndexes.
    def exitLoadedTableIndexes(self, ctx:mysqlParser.LoadedTableIndexesContext):
        pass


    # Enter a parse tree produced by mysqlParser#simpleDescribeStatement.
    def enterSimpleDescribeStatement(self, ctx:mysqlParser.SimpleDescribeStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#simpleDescribeStatement.
    def exitSimpleDescribeStatement(self, ctx:mysqlParser.SimpleDescribeStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#fullDescribeStatement.
    def enterFullDescribeStatement(self, ctx:mysqlParser.FullDescribeStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#fullDescribeStatement.
    def exitFullDescribeStatement(self, ctx:mysqlParser.FullDescribeStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#helpStatement.
    def enterHelpStatement(self, ctx:mysqlParser.HelpStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#helpStatement.
    def exitHelpStatement(self, ctx:mysqlParser.HelpStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#useStatement.
    def enterUseStatement(self, ctx:mysqlParser.UseStatementContext):
        pass

    # Exit a parse tree produced by mysqlParser#useStatement.
    def exitUseStatement(self, ctx:mysqlParser.UseStatementContext):
        pass


    # Enter a parse tree produced by mysqlParser#describeStatements.
    def enterDescribeStatements(self, ctx:mysqlParser.DescribeStatementsContext):
        pass

    # Exit a parse tree produced by mysqlParser#describeStatements.
    def exitDescribeStatements(self, ctx:mysqlParser.DescribeStatementsContext):
        pass


    # Enter a parse tree produced by mysqlParser#describeConnection.
    def enterDescribeConnection(self, ctx:mysqlParser.DescribeConnectionContext):
        pass

    # Exit a parse tree produced by mysqlParser#describeConnection.
    def exitDescribeConnection(self, ctx:mysqlParser.DescribeConnectionContext):
        pass


    # Enter a parse tree produced by mysqlParser#fullId.
    def enterFullId(self, ctx:mysqlParser.FullIdContext):
        pass

    # Exit a parse tree produced by mysqlParser#fullId.
    def exitFullId(self, ctx:mysqlParser.FullIdContext):
        pass


    # Enter a parse tree produced by mysqlParser#tableName.
    def enterTableName(self, ctx:mysqlParser.TableNameContext):
        pass

    # Exit a parse tree produced by mysqlParser#tableName.
    def exitTableName(self, ctx:mysqlParser.TableNameContext):
        pass


    # Enter a parse tree produced by mysqlParser#fullColumnName.
    def enterFullColumnName(self, ctx:mysqlParser.FullColumnNameContext):
        pass

    # Exit a parse tree produced by mysqlParser#fullColumnName.
    def exitFullColumnName(self, ctx:mysqlParser.FullColumnNameContext):
        pass


    # Enter a parse tree produced by mysqlParser#indexColumnName.
    def enterIndexColumnName(self, ctx:mysqlParser.IndexColumnNameContext):
        pass

    # Exit a parse tree produced by mysqlParser#indexColumnName.
    def exitIndexColumnName(self, ctx:mysqlParser.IndexColumnNameContext):
        pass


    # Enter a parse tree produced by mysqlParser#userName.
    def enterUserName(self, ctx:mysqlParser.UserNameContext):
        pass

    # Exit a parse tree produced by mysqlParser#userName.
    def exitUserName(self, ctx:mysqlParser.UserNameContext):
        pass


    # Enter a parse tree produced by mysqlParser#mysqlVariable.
    def enterMysqlVariable(self, ctx:mysqlParser.MysqlVariableContext):
        pass

    # Exit a parse tree produced by mysqlParser#mysqlVariable.
    def exitMysqlVariable(self, ctx:mysqlParser.MysqlVariableContext):
        pass


    # Enter a parse tree produced by mysqlParser#charsetName.
    def enterCharsetName(self, ctx:mysqlParser.CharsetNameContext):
        pass

    # Exit a parse tree produced by mysqlParser#charsetName.
    def exitCharsetName(self, ctx:mysqlParser.CharsetNameContext):
        pass


    # Enter a parse tree produced by mysqlParser#collationName.
    def enterCollationName(self, ctx:mysqlParser.CollationNameContext):
        pass

    # Exit a parse tree produced by mysqlParser#collationName.
    def exitCollationName(self, ctx:mysqlParser.CollationNameContext):
        pass


    # Enter a parse tree produced by mysqlParser#engineName.
    def enterEngineName(self, ctx:mysqlParser.EngineNameContext):
        pass

    # Exit a parse tree produced by mysqlParser#engineName.
    def exitEngineName(self, ctx:mysqlParser.EngineNameContext):
        pass


    # Enter a parse tree produced by mysqlParser#uuidSet.
    def enterUuidSet(self, ctx:mysqlParser.UuidSetContext):
        pass

    # Exit a parse tree produced by mysqlParser#uuidSet.
    def exitUuidSet(self, ctx:mysqlParser.UuidSetContext):
        pass


    # Enter a parse tree produced by mysqlParser#xid.
    def enterXid(self, ctx:mysqlParser.XidContext):
        pass

    # Exit a parse tree produced by mysqlParser#xid.
    def exitXid(self, ctx:mysqlParser.XidContext):
        pass


    # Enter a parse tree produced by mysqlParser#xuidStringId.
    def enterXuidStringId(self, ctx:mysqlParser.XuidStringIdContext):
        pass

    # Exit a parse tree produced by mysqlParser#xuidStringId.
    def exitXuidStringId(self, ctx:mysqlParser.XuidStringIdContext):
        pass


    # Enter a parse tree produced by mysqlParser#authPlugin.
    def enterAuthPlugin(self, ctx:mysqlParser.AuthPluginContext):
        pass

    # Exit a parse tree produced by mysqlParser#authPlugin.
    def exitAuthPlugin(self, ctx:mysqlParser.AuthPluginContext):
        pass


    # Enter a parse tree produced by mysqlParser#uid.
    def enterUid(self, ctx:mysqlParser.UidContext):
        pass

    # Exit a parse tree produced by mysqlParser#uid.
    def exitUid(self, ctx:mysqlParser.UidContext):
        pass


    # Enter a parse tree produced by mysqlParser#simpleId.
    def enterSimpleId(self, ctx:mysqlParser.SimpleIdContext):
        pass

    # Exit a parse tree produced by mysqlParser#simpleId.
    def exitSimpleId(self, ctx:mysqlParser.SimpleIdContext):
        pass


    # Enter a parse tree produced by mysqlParser#dottedId.
    def enterDottedId(self, ctx:mysqlParser.DottedIdContext):
        pass

    # Exit a parse tree produced by mysqlParser#dottedId.
    def exitDottedId(self, ctx:mysqlParser.DottedIdContext):
        pass


    # Enter a parse tree produced by mysqlParser#decimalLiteral.
    def enterDecimalLiteral(self, ctx:mysqlParser.DecimalLiteralContext):
        pass

    # Exit a parse tree produced by mysqlParser#decimalLiteral.
    def exitDecimalLiteral(self, ctx:mysqlParser.DecimalLiteralContext):
        pass


    # Enter a parse tree produced by mysqlParser#fileSizeLiteral.
    def enterFileSizeLiteral(self, ctx:mysqlParser.FileSizeLiteralContext):
        pass

    # Exit a parse tree produced by mysqlParser#fileSizeLiteral.
    def exitFileSizeLiteral(self, ctx:mysqlParser.FileSizeLiteralContext):
        pass


    # Enter a parse tree produced by mysqlParser#stringLiteral.
    def enterStringLiteral(self, ctx:mysqlParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by mysqlParser#stringLiteral.
    def exitStringLiteral(self, ctx:mysqlParser.StringLiteralContext):
        pass


    # Enter a parse tree produced by mysqlParser#booleanLiteral.
    def enterBooleanLiteral(self, ctx:mysqlParser.BooleanLiteralContext):
        pass

    # Exit a parse tree produced by mysqlParser#booleanLiteral.
    def exitBooleanLiteral(self, ctx:mysqlParser.BooleanLiteralContext):
        pass


    # Enter a parse tree produced by mysqlParser#hexadecimalLiteral.
    def enterHexadecimalLiteral(self, ctx:mysqlParser.HexadecimalLiteralContext):
        pass

    # Exit a parse tree produced by mysqlParser#hexadecimalLiteral.
    def exitHexadecimalLiteral(self, ctx:mysqlParser.HexadecimalLiteralContext):
        pass


    # Enter a parse tree produced by mysqlParser#nullNotnull.
    def enterNullNotnull(self, ctx:mysqlParser.NullNotnullContext):
        pass

    # Exit a parse tree produced by mysqlParser#nullNotnull.
    def exitNullNotnull(self, ctx:mysqlParser.NullNotnullContext):
        pass


    # Enter a parse tree produced by mysqlParser#constant.
    def enterConstant(self, ctx:mysqlParser.ConstantContext):
        pass

    # Exit a parse tree produced by mysqlParser#constant.
    def exitConstant(self, ctx:mysqlParser.ConstantContext):
        pass


    # Enter a parse tree produced by mysqlParser#stringDataType.
    def enterStringDataType(self, ctx:mysqlParser.StringDataTypeContext):
        pass

    # Exit a parse tree produced by mysqlParser#stringDataType.
    def exitStringDataType(self, ctx:mysqlParser.StringDataTypeContext):
        pass


    # Enter a parse tree produced by mysqlParser#dimensionDataType.
    def enterDimensionDataType(self, ctx:mysqlParser.DimensionDataTypeContext):
        pass

    # Exit a parse tree produced by mysqlParser#dimensionDataType.
    def exitDimensionDataType(self, ctx:mysqlParser.DimensionDataTypeContext):
        pass


    # Enter a parse tree produced by mysqlParser#simpleDataType.
    def enterSimpleDataType(self, ctx:mysqlParser.SimpleDataTypeContext):
        pass

    # Exit a parse tree produced by mysqlParser#simpleDataType.
    def exitSimpleDataType(self, ctx:mysqlParser.SimpleDataTypeContext):
        pass


    # Enter a parse tree produced by mysqlParser#collectionDataType.
    def enterCollectionDataType(self, ctx:mysqlParser.CollectionDataTypeContext):
        pass

    # Exit a parse tree produced by mysqlParser#collectionDataType.
    def exitCollectionDataType(self, ctx:mysqlParser.CollectionDataTypeContext):
        pass


    # Enter a parse tree produced by mysqlParser#spatialDataType.
    def enterSpatialDataType(self, ctx:mysqlParser.SpatialDataTypeContext):
        pass

    # Exit a parse tree produced by mysqlParser#spatialDataType.
    def exitSpatialDataType(self, ctx:mysqlParser.SpatialDataTypeContext):
        pass


    # Enter a parse tree produced by mysqlParser#convertedDataType.
    def enterConvertedDataType(self, ctx:mysqlParser.ConvertedDataTypeContext):
        pass

    # Exit a parse tree produced by mysqlParser#convertedDataType.
    def exitConvertedDataType(self, ctx:mysqlParser.ConvertedDataTypeContext):
        pass


    # Enter a parse tree produced by mysqlParser#lengthOneDimension.
    def enterLengthOneDimension(self, ctx:mysqlParser.LengthOneDimensionContext):
        pass

    # Exit a parse tree produced by mysqlParser#lengthOneDimension.
    def exitLengthOneDimension(self, ctx:mysqlParser.LengthOneDimensionContext):
        pass


    # Enter a parse tree produced by mysqlParser#lengthTwoDimension.
    def enterLengthTwoDimension(self, ctx:mysqlParser.LengthTwoDimensionContext):
        pass

    # Exit a parse tree produced by mysqlParser#lengthTwoDimension.
    def exitLengthTwoDimension(self, ctx:mysqlParser.LengthTwoDimensionContext):
        pass


    # Enter a parse tree produced by mysqlParser#lengthTwoOptionalDimension.
    def enterLengthTwoOptionalDimension(self, ctx:mysqlParser.LengthTwoOptionalDimensionContext):
        pass

    # Exit a parse tree produced by mysqlParser#lengthTwoOptionalDimension.
    def exitLengthTwoOptionalDimension(self, ctx:mysqlParser.LengthTwoOptionalDimensionContext):
        pass


    # Enter a parse tree produced by mysqlParser#uidList.
    def enterUidList(self, ctx:mysqlParser.UidListContext):
        pass

    # Exit a parse tree produced by mysqlParser#uidList.
    def exitUidList(self, ctx:mysqlParser.UidListContext):
        pass


    # Enter a parse tree produced by mysqlParser#tables.
    def enterTables(self, ctx:mysqlParser.TablesContext):
        pass

    # Exit a parse tree produced by mysqlParser#tables.
    def exitTables(self, ctx:mysqlParser.TablesContext):
        pass


    # Enter a parse tree produced by mysqlParser#tablePairs.
    def enterTablePairs(self, ctx:mysqlParser.TablePairsContext):
        pass

    # Exit a parse tree produced by mysqlParser#tablePairs.
    def exitTablePairs(self, ctx:mysqlParser.TablePairsContext):
        pass


    # Enter a parse tree produced by mysqlParser#indexColumnNames.
    def enterIndexColumnNames(self, ctx:mysqlParser.IndexColumnNamesContext):
        pass

    # Exit a parse tree produced by mysqlParser#indexColumnNames.
    def exitIndexColumnNames(self, ctx:mysqlParser.IndexColumnNamesContext):
        pass


    # Enter a parse tree produced by mysqlParser#expressions.
    def enterExpressions(self, ctx:mysqlParser.ExpressionsContext):
        pass

    # Exit a parse tree produced by mysqlParser#expressions.
    def exitExpressions(self, ctx:mysqlParser.ExpressionsContext):
        pass


    # Enter a parse tree produced by mysqlParser#constants.
    def enterConstants(self, ctx:mysqlParser.ConstantsContext):
        pass

    # Exit a parse tree produced by mysqlParser#constants.
    def exitConstants(self, ctx:mysqlParser.ConstantsContext):
        pass


    # Enter a parse tree produced by mysqlParser#simpleStrings.
    def enterSimpleStrings(self, ctx:mysqlParser.SimpleStringsContext):
        pass

    # Exit a parse tree produced by mysqlParser#simpleStrings.
    def exitSimpleStrings(self, ctx:mysqlParser.SimpleStringsContext):
        pass


    # Enter a parse tree produced by mysqlParser#userVariables.
    def enterUserVariables(self, ctx:mysqlParser.UserVariablesContext):
        pass

    # Exit a parse tree produced by mysqlParser#userVariables.
    def exitUserVariables(self, ctx:mysqlParser.UserVariablesContext):
        pass


    # Enter a parse tree produced by mysqlParser#defaultValue.
    def enterDefaultValue(self, ctx:mysqlParser.DefaultValueContext):
        pass

    # Exit a parse tree produced by mysqlParser#defaultValue.
    def exitDefaultValue(self, ctx:mysqlParser.DefaultValueContext):
        pass


    # Enter a parse tree produced by mysqlParser#ifExists.
    def enterIfExists(self, ctx:mysqlParser.IfExistsContext):
        pass

    # Exit a parse tree produced by mysqlParser#ifExists.
    def exitIfExists(self, ctx:mysqlParser.IfExistsContext):
        pass


    # Enter a parse tree produced by mysqlParser#ifNotExists.
    def enterIfNotExists(self, ctx:mysqlParser.IfNotExistsContext):
        pass

    # Exit a parse tree produced by mysqlParser#ifNotExists.
    def exitIfNotExists(self, ctx:mysqlParser.IfNotExistsContext):
        pass


    # Enter a parse tree produced by mysqlParser#specificFunctionCall.
    def enterSpecificFunctionCall(self, ctx:mysqlParser.SpecificFunctionCallContext):
        pass

    # Exit a parse tree produced by mysqlParser#specificFunctionCall.
    def exitSpecificFunctionCall(self, ctx:mysqlParser.SpecificFunctionCallContext):
        pass


    # Enter a parse tree produced by mysqlParser#aggregateFunctionCall.
    def enterAggregateFunctionCall(self, ctx:mysqlParser.AggregateFunctionCallContext):
        pass

    # Exit a parse tree produced by mysqlParser#aggregateFunctionCall.
    def exitAggregateFunctionCall(self, ctx:mysqlParser.AggregateFunctionCallContext):
        pass


    # Enter a parse tree produced by mysqlParser#scalarFunctionCall.
    def enterScalarFunctionCall(self, ctx:mysqlParser.ScalarFunctionCallContext):
        pass

    # Exit a parse tree produced by mysqlParser#scalarFunctionCall.
    def exitScalarFunctionCall(self, ctx:mysqlParser.ScalarFunctionCallContext):
        pass


    # Enter a parse tree produced by mysqlParser#udfFunctionCall.
    def enterUdfFunctionCall(self, ctx:mysqlParser.UdfFunctionCallContext):
        pass

    # Exit a parse tree produced by mysqlParser#udfFunctionCall.
    def exitUdfFunctionCall(self, ctx:mysqlParser.UdfFunctionCallContext):
        pass


    # Enter a parse tree produced by mysqlParser#passwordFunctionCall.
    def enterPasswordFunctionCall(self, ctx:mysqlParser.PasswordFunctionCallContext):
        pass

    # Exit a parse tree produced by mysqlParser#passwordFunctionCall.
    def exitPasswordFunctionCall(self, ctx:mysqlParser.PasswordFunctionCallContext):
        pass


    # Enter a parse tree produced by mysqlParser#simpleFunctionCall.
    def enterSimpleFunctionCall(self, ctx:mysqlParser.SimpleFunctionCallContext):
        pass

    # Exit a parse tree produced by mysqlParser#simpleFunctionCall.
    def exitSimpleFunctionCall(self, ctx:mysqlParser.SimpleFunctionCallContext):
        pass


    # Enter a parse tree produced by mysqlParser#dataTypeFunctionCall.
    def enterDataTypeFunctionCall(self, ctx:mysqlParser.DataTypeFunctionCallContext):
        pass

    # Exit a parse tree produced by mysqlParser#dataTypeFunctionCall.
    def exitDataTypeFunctionCall(self, ctx:mysqlParser.DataTypeFunctionCallContext):
        pass


    # Enter a parse tree produced by mysqlParser#valuesFunctionCall.
    def enterValuesFunctionCall(self, ctx:mysqlParser.ValuesFunctionCallContext):
        pass

    # Exit a parse tree produced by mysqlParser#valuesFunctionCall.
    def exitValuesFunctionCall(self, ctx:mysqlParser.ValuesFunctionCallContext):
        pass


    # Enter a parse tree produced by mysqlParser#caseFunctionCall.
    def enterCaseFunctionCall(self, ctx:mysqlParser.CaseFunctionCallContext):
        pass

    # Exit a parse tree produced by mysqlParser#caseFunctionCall.
    def exitCaseFunctionCall(self, ctx:mysqlParser.CaseFunctionCallContext):
        pass


    # Enter a parse tree produced by mysqlParser#charFunctionCall.
    def enterCharFunctionCall(self, ctx:mysqlParser.CharFunctionCallContext):
        pass

    # Exit a parse tree produced by mysqlParser#charFunctionCall.
    def exitCharFunctionCall(self, ctx:mysqlParser.CharFunctionCallContext):
        pass


    # Enter a parse tree produced by mysqlParser#positionFunctionCall.
    def enterPositionFunctionCall(self, ctx:mysqlParser.PositionFunctionCallContext):
        pass

    # Exit a parse tree produced by mysqlParser#positionFunctionCall.
    def exitPositionFunctionCall(self, ctx:mysqlParser.PositionFunctionCallContext):
        pass


    # Enter a parse tree produced by mysqlParser#substrFunctionCall.
    def enterSubstrFunctionCall(self, ctx:mysqlParser.SubstrFunctionCallContext):
        pass

    # Exit a parse tree produced by mysqlParser#substrFunctionCall.
    def exitSubstrFunctionCall(self, ctx:mysqlParser.SubstrFunctionCallContext):
        pass


    # Enter a parse tree produced by mysqlParser#trimFunctionCall.
    def enterTrimFunctionCall(self, ctx:mysqlParser.TrimFunctionCallContext):
        pass

    # Exit a parse tree produced by mysqlParser#trimFunctionCall.
    def exitTrimFunctionCall(self, ctx:mysqlParser.TrimFunctionCallContext):
        pass


    # Enter a parse tree produced by mysqlParser#weightFunctionCall.
    def enterWeightFunctionCall(self, ctx:mysqlParser.WeightFunctionCallContext):
        pass

    # Exit a parse tree produced by mysqlParser#weightFunctionCall.
    def exitWeightFunctionCall(self, ctx:mysqlParser.WeightFunctionCallContext):
        pass


    # Enter a parse tree produced by mysqlParser#extractFunctionCall.
    def enterExtractFunctionCall(self, ctx:mysqlParser.ExtractFunctionCallContext):
        pass

    # Exit a parse tree produced by mysqlParser#extractFunctionCall.
    def exitExtractFunctionCall(self, ctx:mysqlParser.ExtractFunctionCallContext):
        pass


    # Enter a parse tree produced by mysqlParser#getFormatFunctionCall.
    def enterGetFormatFunctionCall(self, ctx:mysqlParser.GetFormatFunctionCallContext):
        pass

    # Exit a parse tree produced by mysqlParser#getFormatFunctionCall.
    def exitGetFormatFunctionCall(self, ctx:mysqlParser.GetFormatFunctionCallContext):
        pass


    # Enter a parse tree produced by mysqlParser#levelWeightList.
    def enterLevelWeightList(self, ctx:mysqlParser.LevelWeightListContext):
        pass

    # Exit a parse tree produced by mysqlParser#levelWeightList.
    def exitLevelWeightList(self, ctx:mysqlParser.LevelWeightListContext):
        pass


    # Enter a parse tree produced by mysqlParser#levelWeightRange.
    def enterLevelWeightRange(self, ctx:mysqlParser.LevelWeightRangeContext):
        pass

    # Exit a parse tree produced by mysqlParser#levelWeightRange.
    def exitLevelWeightRange(self, ctx:mysqlParser.LevelWeightRangeContext):
        pass


    # Enter a parse tree produced by mysqlParser#aggregateWindowedFunction.
    def enterAggregateWindowedFunction(self, ctx:mysqlParser.AggregateWindowedFunctionContext):
        pass

    # Exit a parse tree produced by mysqlParser#aggregateWindowedFunction.
    def exitAggregateWindowedFunction(self, ctx:mysqlParser.AggregateWindowedFunctionContext):
        pass


    # Enter a parse tree produced by mysqlParser#scalarFunctionName.
    def enterScalarFunctionName(self, ctx:mysqlParser.ScalarFunctionNameContext):
        pass

    # Exit a parse tree produced by mysqlParser#scalarFunctionName.
    def exitScalarFunctionName(self, ctx:mysqlParser.ScalarFunctionNameContext):
        pass


    # Enter a parse tree produced by mysqlParser#passwordFunctionClause.
    def enterPasswordFunctionClause(self, ctx:mysqlParser.PasswordFunctionClauseContext):
        pass

    # Exit a parse tree produced by mysqlParser#passwordFunctionClause.
    def exitPasswordFunctionClause(self, ctx:mysqlParser.PasswordFunctionClauseContext):
        pass


    # Enter a parse tree produced by mysqlParser#functionArgs.
    def enterFunctionArgs(self, ctx:mysqlParser.FunctionArgsContext):
        pass

    # Exit a parse tree produced by mysqlParser#functionArgs.
    def exitFunctionArgs(self, ctx:mysqlParser.FunctionArgsContext):
        pass


    # Enter a parse tree produced by mysqlParser#functionArg.
    def enterFunctionArg(self, ctx:mysqlParser.FunctionArgContext):
        pass

    # Exit a parse tree produced by mysqlParser#functionArg.
    def exitFunctionArg(self, ctx:mysqlParser.FunctionArgContext):
        pass


    # Enter a parse tree produced by mysqlParser#isExpression.
    def enterIsExpression(self, ctx:mysqlParser.IsExpressionContext):
        pass

    # Exit a parse tree produced by mysqlParser#isExpression.
    def exitIsExpression(self, ctx:mysqlParser.IsExpressionContext):
        pass


    # Enter a parse tree produced by mysqlParser#notExpression.
    def enterNotExpression(self, ctx:mysqlParser.NotExpressionContext):
        pass

    # Exit a parse tree produced by mysqlParser#notExpression.
    def exitNotExpression(self, ctx:mysqlParser.NotExpressionContext):
        pass


    # Enter a parse tree produced by mysqlParser#logicalExpression.
    def enterLogicalExpression(self, ctx:mysqlParser.LogicalExpressionContext):
        pass

    # Exit a parse tree produced by mysqlParser#logicalExpression.
    def exitLogicalExpression(self, ctx:mysqlParser.LogicalExpressionContext):
        pass


    # Enter a parse tree produced by mysqlParser#predicateExpression.
    def enterPredicateExpression(self, ctx:mysqlParser.PredicateExpressionContext):
        pass

    # Exit a parse tree produced by mysqlParser#predicateExpression.
    def exitPredicateExpression(self, ctx:mysqlParser.PredicateExpressionContext):
        pass


    # Enter a parse tree produced by mysqlParser#soundsLikePredicate.
    def enterSoundsLikePredicate(self, ctx:mysqlParser.SoundsLikePredicateContext):
        pass

    # Exit a parse tree produced by mysqlParser#soundsLikePredicate.
    def exitSoundsLikePredicate(self, ctx:mysqlParser.SoundsLikePredicateContext):
        pass


    # Enter a parse tree produced by mysqlParser#expressionAtomPredicate.
    def enterExpressionAtomPredicate(self, ctx:mysqlParser.ExpressionAtomPredicateContext):
        pass

    # Exit a parse tree produced by mysqlParser#expressionAtomPredicate.
    def exitExpressionAtomPredicate(self, ctx:mysqlParser.ExpressionAtomPredicateContext):
        pass


    # Enter a parse tree produced by mysqlParser#inPredicate.
    def enterInPredicate(self, ctx:mysqlParser.InPredicateContext):
        pass

    # Exit a parse tree produced by mysqlParser#inPredicate.
    def exitInPredicate(self, ctx:mysqlParser.InPredicateContext):
        pass


    # Enter a parse tree produced by mysqlParser#subqueryComparasionPredicate.
    def enterSubqueryComparasionPredicate(self, ctx:mysqlParser.SubqueryComparasionPredicateContext):
        pass

    # Exit a parse tree produced by mysqlParser#subqueryComparasionPredicate.
    def exitSubqueryComparasionPredicate(self, ctx:mysqlParser.SubqueryComparasionPredicateContext):
        pass


    # Enter a parse tree produced by mysqlParser#betweenPredicate.
    def enterBetweenPredicate(self, ctx:mysqlParser.BetweenPredicateContext):
        pass

    # Exit a parse tree produced by mysqlParser#betweenPredicate.
    def exitBetweenPredicate(self, ctx:mysqlParser.BetweenPredicateContext):
        pass


    # Enter a parse tree produced by mysqlParser#binaryComparasionPredicate.
    def enterBinaryComparasionPredicate(self, ctx:mysqlParser.BinaryComparasionPredicateContext):
        pass

    # Exit a parse tree produced by mysqlParser#binaryComparasionPredicate.
    def exitBinaryComparasionPredicate(self, ctx:mysqlParser.BinaryComparasionPredicateContext):
        pass


    # Enter a parse tree produced by mysqlParser#isNullPredicate.
    def enterIsNullPredicate(self, ctx:mysqlParser.IsNullPredicateContext):
        pass

    # Exit a parse tree produced by mysqlParser#isNullPredicate.
    def exitIsNullPredicate(self, ctx:mysqlParser.IsNullPredicateContext):
        pass


    # Enter a parse tree produced by mysqlParser#likePredicate.
    def enterLikePredicate(self, ctx:mysqlParser.LikePredicateContext):
        pass

    # Exit a parse tree produced by mysqlParser#likePredicate.
    def exitLikePredicate(self, ctx:mysqlParser.LikePredicateContext):
        pass


    # Enter a parse tree produced by mysqlParser#regexpPredicate.
    def enterRegexpPredicate(self, ctx:mysqlParser.RegexpPredicateContext):
        pass

    # Exit a parse tree produced by mysqlParser#regexpPredicate.
    def exitRegexpPredicate(self, ctx:mysqlParser.RegexpPredicateContext):
        pass


    # Enter a parse tree produced by mysqlParser#unaryExpressionAtom.
    def enterUnaryExpressionAtom(self, ctx:mysqlParser.UnaryExpressionAtomContext):
        pass

    # Exit a parse tree produced by mysqlParser#unaryExpressionAtom.
    def exitUnaryExpressionAtom(self, ctx:mysqlParser.UnaryExpressionAtomContext):
        pass


    # Enter a parse tree produced by mysqlParser#mysqlVariableExpressionAtom.
    def enterMysqlVariableExpressionAtom(self, ctx:mysqlParser.MysqlVariableExpressionAtomContext):
        pass

    # Exit a parse tree produced by mysqlParser#mysqlVariableExpressionAtom.
    def exitMysqlVariableExpressionAtom(self, ctx:mysqlParser.MysqlVariableExpressionAtomContext):
        pass


    # Enter a parse tree produced by mysqlParser#defaultExpressionAtom.
    def enterDefaultExpressionAtom(self, ctx:mysqlParser.DefaultExpressionAtomContext):
        pass

    # Exit a parse tree produced by mysqlParser#defaultExpressionAtom.
    def exitDefaultExpressionAtom(self, ctx:mysqlParser.DefaultExpressionAtomContext):
        pass


    # Enter a parse tree produced by mysqlParser#nestedExpressionAtom.
    def enterNestedExpressionAtom(self, ctx:mysqlParser.NestedExpressionAtomContext):
        pass

    # Exit a parse tree produced by mysqlParser#nestedExpressionAtom.
    def exitNestedExpressionAtom(self, ctx:mysqlParser.NestedExpressionAtomContext):
        pass


    # Enter a parse tree produced by mysqlParser#nestedRowExpressionAtom.
    def enterNestedRowExpressionAtom(self, ctx:mysqlParser.NestedRowExpressionAtomContext):
        pass

    # Exit a parse tree produced by mysqlParser#nestedRowExpressionAtom.
    def exitNestedRowExpressionAtom(self, ctx:mysqlParser.NestedRowExpressionAtomContext):
        pass


    # Enter a parse tree produced by mysqlParser#mathExpressionAtom.
    def enterMathExpressionAtom(self, ctx:mysqlParser.MathExpressionAtomContext):
        pass

    # Exit a parse tree produced by mysqlParser#mathExpressionAtom.
    def exitMathExpressionAtom(self, ctx:mysqlParser.MathExpressionAtomContext):
        pass


    # Enter a parse tree produced by mysqlParser#intervalExpressionAtom.
    def enterIntervalExpressionAtom(self, ctx:mysqlParser.IntervalExpressionAtomContext):
        pass

    # Exit a parse tree produced by mysqlParser#intervalExpressionAtom.
    def exitIntervalExpressionAtom(self, ctx:mysqlParser.IntervalExpressionAtomContext):
        pass


    # Enter a parse tree produced by mysqlParser#existsExpessionAtom.
    def enterExistsExpessionAtom(self, ctx:mysqlParser.ExistsExpessionAtomContext):
        pass

    # Exit a parse tree produced by mysqlParser#existsExpessionAtom.
    def exitExistsExpessionAtom(self, ctx:mysqlParser.ExistsExpessionAtomContext):
        pass


    # Enter a parse tree produced by mysqlParser#constantExpressionAtom.
    def enterConstantExpressionAtom(self, ctx:mysqlParser.ConstantExpressionAtomContext):
        pass

    # Exit a parse tree produced by mysqlParser#constantExpressionAtom.
    def exitConstantExpressionAtom(self, ctx:mysqlParser.ConstantExpressionAtomContext):
        pass


    # Enter a parse tree produced by mysqlParser#functionCallExpressionAtom.
    def enterFunctionCallExpressionAtom(self, ctx:mysqlParser.FunctionCallExpressionAtomContext):
        pass

    # Exit a parse tree produced by mysqlParser#functionCallExpressionAtom.
    def exitFunctionCallExpressionAtom(self, ctx:mysqlParser.FunctionCallExpressionAtomContext):
        pass


    # Enter a parse tree produced by mysqlParser#binaryExpressionAtom.
    def enterBinaryExpressionAtom(self, ctx:mysqlParser.BinaryExpressionAtomContext):
        pass

    # Exit a parse tree produced by mysqlParser#binaryExpressionAtom.
    def exitBinaryExpressionAtom(self, ctx:mysqlParser.BinaryExpressionAtomContext):
        pass


    # Enter a parse tree produced by mysqlParser#fullColumnNameExpressionAtom.
    def enterFullColumnNameExpressionAtom(self, ctx:mysqlParser.FullColumnNameExpressionAtomContext):
        pass

    # Exit a parse tree produced by mysqlParser#fullColumnNameExpressionAtom.
    def exitFullColumnNameExpressionAtom(self, ctx:mysqlParser.FullColumnNameExpressionAtomContext):
        pass


    # Enter a parse tree produced by mysqlParser#bitExpressionAtom.
    def enterBitExpressionAtom(self, ctx:mysqlParser.BitExpressionAtomContext):
        pass

    # Exit a parse tree produced by mysqlParser#bitExpressionAtom.
    def exitBitExpressionAtom(self, ctx:mysqlParser.BitExpressionAtomContext):
        pass


    # Enter a parse tree produced by mysqlParser#unaryOperator.
    def enterUnaryOperator(self, ctx:mysqlParser.UnaryOperatorContext):
        pass

    # Exit a parse tree produced by mysqlParser#unaryOperator.
    def exitUnaryOperator(self, ctx:mysqlParser.UnaryOperatorContext):
        pass


    # Enter a parse tree produced by mysqlParser#comparisonOperator.
    def enterComparisonOperator(self, ctx:mysqlParser.ComparisonOperatorContext):
        pass

    # Exit a parse tree produced by mysqlParser#comparisonOperator.
    def exitComparisonOperator(self, ctx:mysqlParser.ComparisonOperatorContext):
        pass


    # Enter a parse tree produced by mysqlParser#logicalOperator.
    def enterLogicalOperator(self, ctx:mysqlParser.LogicalOperatorContext):
        pass

    # Exit a parse tree produced by mysqlParser#logicalOperator.
    def exitLogicalOperator(self, ctx:mysqlParser.LogicalOperatorContext):
        pass


    # Enter a parse tree produced by mysqlParser#bitOperator.
    def enterBitOperator(self, ctx:mysqlParser.BitOperatorContext):
        pass

    # Exit a parse tree produced by mysqlParser#bitOperator.
    def exitBitOperator(self, ctx:mysqlParser.BitOperatorContext):
        pass


    # Enter a parse tree produced by mysqlParser#mathOperator.
    def enterMathOperator(self, ctx:mysqlParser.MathOperatorContext):
        pass

    # Exit a parse tree produced by mysqlParser#mathOperator.
    def exitMathOperator(self, ctx:mysqlParser.MathOperatorContext):
        pass


    # Enter a parse tree produced by mysqlParser#charsetNameBase.
    def enterCharsetNameBase(self, ctx:mysqlParser.CharsetNameBaseContext):
        pass

    # Exit a parse tree produced by mysqlParser#charsetNameBase.
    def exitCharsetNameBase(self, ctx:mysqlParser.CharsetNameBaseContext):
        pass


    # Enter a parse tree produced by mysqlParser#transactionLevelBase.
    def enterTransactionLevelBase(self, ctx:mysqlParser.TransactionLevelBaseContext):
        pass

    # Exit a parse tree produced by mysqlParser#transactionLevelBase.
    def exitTransactionLevelBase(self, ctx:mysqlParser.TransactionLevelBaseContext):
        pass


    # Enter a parse tree produced by mysqlParser#privilegesBase.
    def enterPrivilegesBase(self, ctx:mysqlParser.PrivilegesBaseContext):
        pass

    # Exit a parse tree produced by mysqlParser#privilegesBase.
    def exitPrivilegesBase(self, ctx:mysqlParser.PrivilegesBaseContext):
        pass


    # Enter a parse tree produced by mysqlParser#intervalTypeBase.
    def enterIntervalTypeBase(self, ctx:mysqlParser.IntervalTypeBaseContext):
        pass

    # Exit a parse tree produced by mysqlParser#intervalTypeBase.
    def exitIntervalTypeBase(self, ctx:mysqlParser.IntervalTypeBaseContext):
        pass


    # Enter a parse tree produced by mysqlParser#dataTypeBase.
    def enterDataTypeBase(self, ctx:mysqlParser.DataTypeBaseContext):
        pass

    # Exit a parse tree produced by mysqlParser#dataTypeBase.
    def exitDataTypeBase(self, ctx:mysqlParser.DataTypeBaseContext):
        pass


    # Enter a parse tree produced by mysqlParser#keywordsCanBeId.
    def enterKeywordsCanBeId(self, ctx:mysqlParser.KeywordsCanBeIdContext):
        pass

    # Exit a parse tree produced by mysqlParser#keywordsCanBeId.
    def exitKeywordsCanBeId(self, ctx:mysqlParser.KeywordsCanBeIdContext):
        pass


    # Enter a parse tree produced by mysqlParser#functionNameBase.
    def enterFunctionNameBase(self, ctx:mysqlParser.FunctionNameBaseContext):
        pass

    # Exit a parse tree produced by mysqlParser#functionNameBase.
    def exitFunctionNameBase(self, ctx:mysqlParser.FunctionNameBaseContext):
        pass


