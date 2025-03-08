import streamlit as st

def main():
    st.title("GST Liability Bot for Immovable Properties")
    st.write("Welcome to the GST Liability Assistant!")
    ask_type_of_property()

def ask_type_of_property():
    st.subheader("Type of Property:")
    property_type = st.radio("Select the type of property:", ["Residential", "Commercial"])
    
    if property_type == "Residential":
        handle_residential()
    elif property_type == "Commercial":
        handle_commercial()

def handle_residential():
    st.subheader("Who is the provider of services?")
    provider = st.radio("Select the provider:", ["Government", "Trust (Registered u/s 12AA/10(23C)(v)/23BB)", "Others"])
    
    if provider == "Government":
        st.success("**Answer:** GST is payable by recipients of service (RCM).")
    elif provider == "Trust (Registered u/s 12AA/10(23C)(v)/23BB)":
        handle_residential_trust()
    elif provider == "Others":
        handle_residential_others()

def handle_residential_trust():
    st.subheader("Select the rent type:")
    rent_type = st.radio("Choose the rent type:", ["Room rent below 1000 per day", "Others"])
    
    if rent_type == "Room rent below 1000 per day":
        st.success("**Answer:** Exempt.")
    else:
        st.success("**Answer:** Taxable as FCM basis.")

def handle_residential_others():
    st.subheader("Nature of property:")
    property_nature = st.radio("Select the nature of property:", ["As Hostel", "Other than Hostel"])
    
    if property_nature == "As Hostel":
        handle_residential_others_hostel()
    elif property_nature == "Other than Hostel":
        handle_residential_others_non_hostel()

def handle_residential_others_hostel():
    st.subheader("Service provider registration status:")
    registration_status = st.radio("Select registration status:", ["Registered under GST", "Unregistered under GST"])
    
    if registration_status == "Registered under GST":
        handle_hostel_registered()
    elif registration_status == "Unregistered under GST":
        handle_hostel_unregistered()

def handle_hostel_registered():
    st.subheader("To whom have services been provided?")
    service_recipient = st.radio("Select the recipient:", ["Registered under GST", "Unregistered under GST"])
    
    if service_recipient in ["Registered under GST", "Unregistered under GST"]:
        handle_beneficiary_type()

def handle_hostel_unregistered():
    st.subheader("To whom have services been provided?")
    service_recipient = st.radio("Select the recipient:", ["Registered under GST", "Unregistered under GST"])
    
    if service_recipient == "Registered under GST":
        handle_beneficiary_type()
    elif service_recipient == "Unregistered under GST":
        st.success("**Answer:** Exempt.")

def handle_beneficiary_type():
    st.subheader("Select beneficiary type:")
    beneficiary_type = st.radio("Choose the beneficiary type:", ["By education institutions", "Other than educational institution"])
    
    if beneficiary_type == "By education institutions":
        st.success("**Answer:** Exempt.")
    else:
        handle_rent_service_value()

def handle_rent_service_value():
    st.subheader("Select rent/service value option:")
    rent_value = st.radio("Choose the rent value:", ["Value of services up to Rs.20000 with minimum stay of 90 days", "Other than this"])
    
    if rent_value == "Value of services up to Rs.20000 with minimum stay of 90 days":
        st.success("**Answer:** Exempt.")
    else:
        st.success("**Answer:** Recipient is liable for tax under RCM.")

def handle_residential_others_non_hostel():
    st.subheader("Select usage type:")
    usage_type = st.radio("Choose the usage type:", ["For personal residence", "Not for personal residence", "Commercial use"])
    
    if usage_type == "For personal residence":
        st.success("**Answer:** Exempt.")
    elif usage_type == "Not for personal residence":
        handle_non_personal_residence()
    elif usage_type == "Commercial use":
        handle_commercial_use()

def handle_non_personal_residence():
    st.subheader("Service provider registration status:")
    registration_status = st.radio("Select registration status:", ["Registered under GST", "Unregistered under GST"])
    
    if registration_status == "Registered under GST":
        handle_non_personal_registered()
    elif registration_status == "Unregistered under GST":
        handle_non_personal_unregistered()

def handle_non_personal_registered():
    st.subheader("To whom is the service provided?")
    service_recipient = st.radio("Select the recipient:", ["Registered under GST", "Not registered under GST"])
    
    if service_recipient == "Registered under GST":
        st.success("**Answer:** GST is payable on RCM basis; however, if a director provides renting services in personal capacity then no RCM applies.")
    elif service_recipient == "Not registered under GST":
        st.success("**Answer:** Exempt.")

def handle_non_personal_unregistered():
    st.subheader("To whom is the service provided?")
    service_recipient = st.radio("Select the recipient:", ["Registered under GST", "Not registered under GST"])
    
    if service_recipient == "Registered under GST":
        st.success("**Answer:** GST is payable on RCM basis; however, if a director provides renting services in personal capacity then no RCM applies.")
    elif service_recipient == "Not registered under GST":
        st.success("**Answer:** Exempt.")

def handle_commercial_use():
    st.subheader("Service provider registration status:")
    registration_status = st.radio("Select registration status:", ["Registered under GST", "Unregistered under GST"])
    
    if registration_status == "Registered under GST":
        handle_commercial_use_registered()
    elif registration_status == "Unregistered under GST":
        handle_commercial_use_unregistered()

def handle_commercial_use_registered():
    st.subheader("To whom is the service provided?")
    service_recipient = st.radio("Select the recipient:", ["Registered under GST", "Not registered under GST"])
    
    if service_recipient == "Registered under GST":
        st.success("**Answer:** Liable as RCM.")
    elif service_recipient == "Not registered under GST":
        st.success("**Answer:** Liable as forward chargeable method (FCM).")

def handle_commercial_use_unregistered():
    st.subheader("To whom is the service provided?")
    service_recipient = st.radio("Select the recipient:", ["Registered under GST", "Not registered under GST"])
    
    if service_recipient == "Registered under GST":
        st.success("**Answer:** Liable as RCM.")
    elif service_recipient == "Not registered under GST":
        st.success("**Answer:** Exempt.")

def handle_commercial():
    st.subheader("Who is the provider of services?")
    provider = st.radio("Select the provider:", ["Government", "Trust (Registered u/s 12AA/10(23C)(v)/23BB)", "Others"])
    
    if provider == "Government":
        st.success("**Answer:** GST is payable by recipients of service (RCM).")
    elif provider == "Trust (Registered u/s 12AA/10(23C)(v)/23BB)":
        handle_commercial_trust()
    elif provider == "Others":
        handle_commercial_others()

def handle_commercial_trust():
    st.subheader("Select rent type:")
    rent_type = st.radio("Choose the rent type:", ["Room rent below 1000 per day and community hall/open area rent per day below 10000", "Others"])
    
    if rent_type == "Room rent below 1000 per day and community hall/open area rent per day below 10000":
        st.success("**Answer:** Exempt.")
    else:
        st.success("**Answer:** Taxable as FCM basis.")

def handle_commercial_others():
    st.subheader("Service provider registration status:")
    registration_status = st.radio("Select registration status:", ["Registered under GST", "Unregistered under GST"])
    
    if registration_status == "Registered under GST":
        st.success("**Answer:** Taxable as forward charge method (FCM).")
    elif registration_status == "Unregistered under GST":
        handle_commercial_unregistered()

def handle_commercial_unregistered():
    st.subheader("To whom is the service provided?")
    service_recipient = st.radio("Select the recipient:", ["Registered under GST", "Not registered under GST"])
    
    if service_recipient == "Registered under GST":
        handle_recipient_registration_type()
    elif service_recipient == "Not registered under GST":
        st.success("**Answer:** Exempt.")

def handle_recipient_registration_type():
    st.subheader("Select service recipient registration type:")
    registration_type = st.radio("Choose the registration type:", ["Regular registered", "Composition registered"])
    
    if registration_type == "Regular registered":
        st.success("**Answer:** Taxable as recipient liable under RCM.")
    elif registration_type == "Composition registered":
        st.success("**Answer:** Exempt.")

if __name__ == "__main__":
    main()