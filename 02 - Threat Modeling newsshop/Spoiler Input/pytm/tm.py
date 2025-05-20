from pytm import TM, Boundary, Actor, Process, Datastore, Dataflow, Data, Classification, Lifetime, Server, DatastoreType

tm = TM("ThreatModelNewsshop")

internet_b =  Boundary(
                name="Internet"
              )

frontend_b =  Boundary(
                name="Frontend",
                inBoundary=internet_b
              )

backend_b  =  Boundary(
                name="Backend"
              )

datastore_b = Boundary(
                name="Datastore",
                inBoundary=backend_b
              )


admin_credentials_d = Data(
                        name="Admin Credentials",
                        description="",
                        classification=Classification.SENSITIVE,
                        isPII=True,
                        isCredentials=True,
                        credentialsLife=Lifetime.LONG,
                        isStored=True,
                        isSourceEncryptedAtRest=False,
                        isDestEncryptedAtRest=True,
                      )

newsletter_d = Data(
                        name="Newsletter Data",
                        description="",
                        classification=Classification.RESTRICTED,
                        isPII=False,
                        isCredentials=False,
                        credentialsLife=Lifetime.LONG,
                        isStored=True,
                        isSourceEncryptedAtRest=False,
                        isDestEncryptedAtRest=False,
                      )



user_browser_a =  Actor(
                    name="UserBrowser",
                    inBoundary=internet_b
                  )

subscribe_p       = Process(
                      name="SubscribeVue",
                      inBoundary=frontend_b,
                      data=newsletter_d,
                    )

admin_p           = Process(
                      name="AdminVue",
                      inBoundary=frontend_b
                    )

newsletter_ctl_p  = Process(
                      name="NewsletterController",
                      inBoundary=backend_b,
                      data=newsletter_d,
                    )

security_cfg_p    = Process(
                      name="SecurityConfig",
                      inBoundary=backend_b,
                    )

newsletter_repo_p = Process(
                      name="NewsletterRepository",
                      inBoundary=backend_b,
                      data=newsletter_d,
                    )

password_repo_p   = Process(
                      name="PasswordRepository",
                      inBoundary=backend_b,
                    )

database_ds = Datastore(
                name="Database",
                inBoundary=datastore_b,
                inScope=True,
                isEncrypted=False,
                storesPII=True,
                data = [admin_credentials_d, newsletter_d],
                type=DatastoreType.SQL,
              )

user_to_subscribe_df =  Dataflow(user_browser_a, subscribe_p, "HTTP: subscribe",
                          protocol="HTTP",
                          dstPort=80,
                          data=newsletter_d,
                        )

user_to_admin_df     =  Dataflow(user_browser_a, admin_p, "HTTP: admin",
                          protocol="HTTP",
                          dstPort=80,
                          data=admin_credentials_d,
                        )

subscribe_to_ctl_df  =  Dataflow(subscribe_p, newsletter_ctl_p, "HTTP",
                          protocol="HTTP",
                          dstPort=80,
                          data=newsletter_d,
                        )

admin_to_ctl_df      =  Dataflow(admin_p, newsletter_ctl_p, "HTTP",
                          protocol="HTTP",
                          dstPort=80,
                          data=admin_credentials_d,
                        )

ctl_to_sec_df        =  Dataflow(newsletter_ctl_p, security_cfg_p, "Validation request",
                        )

sec_to_ctl_df        =  Dataflow(security_cfg_p, newsletter_ctl_p, "Validation result / Access control",
                        )

ctl_to_pw_repo_df    =  Dataflow(newsletter_ctl_p, password_repo_p, "Read/Write password hashes",
                        )

ctl_to_news_repo_df  =  Dataflow(newsletter_ctl_p, newsletter_repo_p, "Read/Write newsletter entries",
                          data=newsletter_d,
                        )

pw_repo_to_db_df     =  Dataflow(password_repo_p, database_ds, "Persist hashes",
                        )

news_repo_to_db_df   =  Dataflow(newsletter_repo_p, database_ds, "Persist newsletter data",
                          data=newsletter_d,
                        )


if __name__ == "__main__":
    tm.process()