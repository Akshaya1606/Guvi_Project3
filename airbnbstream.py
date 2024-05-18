import pandas as pd
import streamlit as st
import plotly.express as px
from datetime import datetime


staydetail = pd.read_excel('Stay_Details_Project3.xlsx')
Reviewdetail=pd.read_excel('Review_Details_Project3.xlsx')

place_loc=list(set(staydetail['Country']))

st.set_page_config(
        page_title="Airbnb Analysis",
        page_icon="Home",
        layout="wide",
    )
st.markdown("<h1 style='text-align: center; color: red;'>AirBnb Analysis</h1>", unsafe_allow_html=True)
first=['About','Stay','Some Analysis']
tabs=st.tabs(first)
with tabs[0]:
    st.image(r"C:\Users\Akshaya\Downloads\airbnb_logo_detail.jpg")
    st.header("Airbnb ")
    st.write("""**Airbnb, Inc. is an American company operating an online marketplace for short- and long-term homestays and experiences. 
             The company acts as a broker and charges a commission from each booking. 
             The company was founded in 2008 by Brian Chesky, Nathan Blecharczyk, and Joe Gebbia. Airbnb is a shortened version of its original name, AirBedandBreakfast.com. 
             Airbnb is the most well-known company for short-term housing rentals.**""")
    st.write("""**This project aims to analyze Airbnb data using MongoDB Atlas, perform data cleaning and preparation, develop interactive geospatial visualizations, 
             and create dynamic plots to gain insights into pricing variations, availability patterns, 
             and location-based trends.**""")
with tabs[1]:
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        place=st.selectbox("Where",(place_loc))
    with col2:
        selected_date = st.date_input("Select Checkin Date",datetime.today())
    with col3:
         selected_date = st.date_input("Select Checkout Date",datetime.today())
    with col4:
        with st.popover("Who"):
            Adults=st.select_slider("Adults,Age 13 and above",(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16))
            Child=st.select_slider("Child, above 2 and below 13",(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16))
            Infant=st.select_slider("Infant,below 2",(0,1,2,3,4,5))
    with col5:
        st.button("Search")

    if "Search":
        home_opl=[]
        home_opl.append('All Options')
        home_opl.extend(list(set(staydetail['Property_type'])))
        home_op=st.selectbox("Select the property type",(home_opl))
        col1,col2=st.columns(2)

        

        with col1:
            
            if home_op=='All Options':
                filtered_rows=staydetail.loc[staydetail['Country'].apply(lambda x: x==place)].reset_index(drop=True)

            else:
                filtered_rows=staydetail.loc[staydetail['Country'].apply(lambda x: x==place)].reset_index(drop=True)
                filtered_rows=filtered_rows.loc[filtered_rows['Property_type'].apply(lambda x: x==home_op)]
                filtered_rows.reset_index(drop=True, inplace=True)
            
            display={'Stay_name':[],'Property_Type':[],'Number of Bedrooms':[],'Number of Beds':[],'Price Details per Room':[],'Rating out of 100':[]}
            display['Stay_name']=filtered_rows['Stay_name']
            display['Property_Type']=filtered_rows['Property_type']
            display['Number of Bedrooms']=filtered_rows['Bedrooms']
            display['Number of Beds']=filtered_rows['Beds']
            display['Price Details per Room']=filtered_rows['Price']
            display['Rating out of 100']=filtered_rows['Review_rating_100']

            st.dataframe(display)

            unique_names = filtered_rows['Stay_name'].unique()

            selected_name = st.sidebar.selectbox("Select a name", unique_names)

        with col2:
            try:
                df = {'latitude':[],'longitude':[],'Price':[],'Property_name':[]}
                df['longitude'] = filtered_rows['Cordinates'].apply(lambda coord: float(coord.split(',')[0][1:]))
                df['latitude'] = filtered_rows['Cordinates'].apply(lambda coord: float(coord.split(',')[1][:-1]))
                df["Price"]=filtered_rows['Price']
                df['Property_name']=filtered_rows['Stay_name']
        # Create a map with the data
                fig = px.scatter_mapbox(df,lat='latitude',lon='longitude',color='Price',zoom=8, center={'lat': df['latitude'][0], 'lon': df['longitude'][0]},mapbox_style='carto-positron',color_continuous_scale='Plasma_r',hover_data=['Price','Property_name'])
                fig.update_geos(
            resolution=50,
            showcoastlines=True,
            coastlinecolor="RebeccaPurple",
            showland=True,
            landcolor="LightGrey",
            showocean=True,
            oceancolor="LightBlue",
            showlakes=True,
            lakecolor="LightBlue",
            showcountries=True)
                fig.update_geos(projection_scale=500)
                st.plotly_chart(fig,use_container_width=True)
            except Exception as e:
                st.write(f"{e}")
                st.warning('No such property available')
        
        if selected_name is not None and tabs[1]:
                selected_row = filtered_rows[filtered_rows['Stay_name'] == selected_name].iloc[0]
                amminities=[]
                amminities=map(str, selected_row['Amenities'].split(','))
                st.header(f"Name of the property: {selected_row['Stay_name']}")
                st.image(f"{selected_row['Stay_image']}")
                st.header(f"{selected_row['Property_type']}")
                st.write(f"**Hosted by {selected_row['Host_Name']}**")
                st.write(f"**Cancellation Policy:** {selected_row['Cancellation_policy']}")
                st.header("Description")
                st.write(f"{selected_row['Stay_description']}")
                st.write(f"**Neighbourhood Description**{selected_row['Neighborhood_description']}")
                st.write(f"**Summary:** {selected_row['Summary']}")
                st.write(f"**House Rules:** {selected_row['House_rules']}")
                st.write(f"**Transit_details to the property:** {selected_row['Transit_detail']}")
                st.write(f"**Accesible  places from the Stay:** {selected_row['Access_from_Stay']}")
                if selected_row['Can_accomodate']==0:
                    price1=(Adults+Child)*selected_row['Price']
                else:
                    price1=(Adults+Child)/selected_row['Can_accomodate']*selected_row['Price']
                st.write(f"**Price Details for Selected number of {Adults+Child} persons = {price1} per day**")
                st.write(f"**Cleaning fee {selected_row['Cleaning_fee']}**")
                st.write(f"**Security deposit :{selected_row['Security_deposit']}**")
                st.header("What this place offers")
                for x in amminities:
                    st.write(":point_right:",x)
                
                st.header("Host Details")
                st.write(f"**Host Name {selected_row['Host_Name']}**")
                st.write(f"**Location** {selected_row['Host_location']}")
                st.write("**Host About**")
                st.write(f"{selected_row['Host_about']}")
                st.write(f"**Host Verification methods** {selected_row['Host_verification']}")

                st.header("Reviews")
                st.write(f"NumberOfReviews {selected_row['NumberOfReviews']}")
                st.write(f":star: Rating on 100: {selected_row['Review_rating_100']}")
                st.write(f":star: Review on Accuracy: {selected_row['Review_Accuracy']}")
                st.write(f":star: Review on cleanliness: {selected_row['Review_cleanliness']}")
                st.write(f":star: Review on Location: {selected_row['Review_Location']}")
                st.write(f":star: Review on communication: {selected_row['Review_communication']}")
                st.write(f":star: Review on checkin: {selected_row['Review_checkin']}")
                st.write(f":star: Review on value: {selected_row['Review_value']}")
                x1=selected_row['Stay_id']
                filtered_review=Reviewdetail.loc[Reviewdetail['Stay_id'].apply(lambda x: x==x1)].reset_index(drop=True)
                tran=filtered_review.T
                st.dataframe(tran)


                st.write("Where you will be")
                
                x, y = map(float, selected_row['Cordinates'].strip('[]').split(', '))
                df = {'latitude':[y],'longitude':[x],'Place':[selected_row['Stay_name']],'Price':[selected_row['Price']]}
                fig = px.density_mapbox(df,lat='latitude',lon='longitude',zoom=8, center={'lat': y, 'lon':x},mapbox_style='carto-positron')
                #,center={'lat': df['latitude'], 'lon': df['longitude']}
                fig.update_geos(
            resolution=50,
            showcountries=True,
            showcoastlines=True,
            coastlinecolor="RebeccaPurple",
            showland=True,
            landcolor="LightGrey",
            showocean=True,
            oceancolor="LightBlue",
            showlakes=True,
            lakecolor="LightBlue")
                st.plotly_chart(fig,use_container_width=True)


with tabs[2]:
    st.header("Some Valubale Insights from the data")

    st.header("Price wise analysis in each Country")
    place_loc1=list(set(staydetail['Country']))
    place1=st.selectbox("Select Place",(place_loc1))
    df = {'latitude':[],'longitude':[],'Price':[],'Property_name':[]}
    filtered_rows1=staydetail.loc[staydetail['Country'].apply(lambda x: x==place1)].reset_index(drop=True)
    df['longitude'] = filtered_rows1['Cordinates'].apply(lambda coord: float(coord.split(',')[0][1:]))
    df['latitude'] = filtered_rows1['Cordinates'].apply(lambda coord: float(coord.split(',')[1][:-1]))
    df["Price"]=filtered_rows1['Price']
    df['Property_name']=filtered_rows1['Stay_name']
    fig = px.scatter_mapbox(df,lat='latitude',lon='longitude',zoom=8,color='Price', center={'lat': df['latitude'][0], 'lon': df['longitude'][0]},mapbox_style='carto-positron',color_continuous_scale='temps',hover_data=['Price','Property_name'],size='Price')
    st.plotly_chart(fig,use_container_width=True)

    st.header("Price wise distribution based on property type")

    df1={'Property_type':[],'Price':[]}
    df1['Property_type']=filtered_rows1['Property_type']
    df1['Price']=filtered_rows1['Price']

    fig=px.bar(df1,x='Property_type',y='Price',color_continuous_scale='Reds',hover_data=['Property_type','Price'])
    st.plotly_chart(fig,use_container_width=True)







        
