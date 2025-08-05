import streamlit as st

# Configure the page
st.set_page_config(
    page_title="Your Bank - CRM Portal",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
<style>
    .header {
        color: #2c3e50;
        text-align: center;
        margin-bottom: 30px;
    }
    .account-card {
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    .btn-edit {
        background-color: #3498db;
        color: white;
        border: none;
        padding: 8px 16px;
        border-radius: 5px;
        cursor: pointer;
    }
    .btn-save {
        background-color: #27ae60;
        color: white;
        border: none;
        padding: 8px 16px;
        border-radius: 5px;
        cursor: pointer;
        margin-right: 10px;
    }
    .btn-cancel {
        background-color: #e74c3c;
        color: white;
        border: none;
        padding: 8px 16px;
        border-radius: 5px;
        cursor: pointer;
    }
    .status-approved {
        color: #27ae60;
        font-weight: bold;
    }
    .status-rejected {
        color: #e74c3c;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Session state management
if 'edit_mode' not in st.session_state:
    st.session_state.edit_mode = False
if 'loan_status' not in st.session_state:
    st.session_state.loan_status = "Pending"

def main():
    st.title("Your Bank - Customer Relationship Management")
    
    # Display account information
    st.markdown("""
    <div class="account-card">
        <h3>Customer Account</h3>
        <p><strong>Account ID:</strong> ACC-7H28-4926-5831</p>
        <p><strong>Customer Name:</strong> John Michael Doe</p>
        <p><strong>Current Loan Status:</strong> <span class="status-{status}">{status}</span></p>
    </div>
    """.format(status=st.session_state.loan_status.lower()), unsafe_allow_html=True)
    
    # Edit button logic
    if not st.session_state.edit_mode:
        if st.button("✏️ Edit Loan Status", key="edit_btn"):
            st.session_state.edit_mode = True
            st.rerun()
    else:
        with st.form("edit_form"):
            st.subheader("Update Loan Status")
            
            # Dropdown for loan status
            new_status = st.selectbox(
                "Select Loan Status",
                ["Approved", "Rejected", "Pending"],
                index=["Approved", "Rejected", "Pending"].index(st.session_state.loan_status)
            )
            
            # Action buttons
            col1, col2 = st.columns(2)
            with col1:
                if st.form_submit_button("💾 Save Changes", type="primary"):
                    st.session_state.loan_status = new_status
                    st.session_state.edit_mode = False
                    st.rerun()
            with col2:
                if st.form_submit_button("❌ Cancel"):
                    st.session_state.edit_mode = False
                    st.rerun()

if __name__ == "__main__":
    main()