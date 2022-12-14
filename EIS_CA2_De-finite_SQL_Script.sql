USE [master]
GO
/****** Object:  Database [Definite CA2]    Script Date: 16/7/2020 10:02:06 PM ******/
CREATE DATABASE [Definite CA2]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'Definite CA2', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL12.MSSQLSERVER\MSSQL\DATA\Definite CA2.mdf' , SIZE = 4096KB , MAXSIZE = UNLIMITED, FILEGROWTH = 1024KB )
 LOG ON 
( NAME = N'Definite CA2_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL12.MSSQLSERVER\MSSQL\DATA\Definite CA2.ldf' , SIZE = 1024KB , MAXSIZE = 2048GB , FILEGROWTH = 10%)
GO
ALTER DATABASE [Definite CA2] SET COMPATIBILITY_LEVEL = 120
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [Definite CA2].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [Definite CA2] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [Definite CA2] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [Definite CA2] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [Definite CA2] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [Definite CA2] SET ARITHABORT OFF 
GO
ALTER DATABASE [Definite CA2] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [Definite CA2] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [Definite CA2] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [Definite CA2] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [Definite CA2] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [Definite CA2] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [Definite CA2] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [Definite CA2] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [Definite CA2] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [Definite CA2] SET  DISABLE_BROKER 
GO
ALTER DATABASE [Definite CA2] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [Definite CA2] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [Definite CA2] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [Definite CA2] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [Definite CA2] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [Definite CA2] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [Definite CA2] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [Definite CA2] SET RECOVERY FULL 
GO
ALTER DATABASE [Definite CA2] SET  MULTI_USER 
GO
ALTER DATABASE [Definite CA2] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [Definite CA2] SET DB_CHAINING OFF 
GO
ALTER DATABASE [Definite CA2] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [Definite CA2] SET TARGET_RECOVERY_TIME = 0 SECONDS 
GO
ALTER DATABASE [Definite CA2] SET DELAYED_DURABILITY = DISABLED 
GO
EXEC sys.sp_db_vardecimal_storage_format N'Definite CA2', N'ON'
GO
USE [Definite CA2]
GO
/****** Object:  Table [dbo].[Account_information2]    Script Date: 16/7/2020 10:02:07 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[Account_information2](
	[Account_id] [varchar](max) NULL,
	[Account_name] [varchar](max) NULL,
	[Password] [varchar](max) NULL,
	[Email] [varchar](max) NULL,
	[Account_balance] [varchar](max) NULL,
	[Walletgroup_name] [varchar](max) NULL,
	[Walletgroup_id] [varchar](max) NULL,
	[Saver_points] [varchar](max) NULL,
	[Tier_level] [varchar](max) NULL,
	[Saver_points_spent] [varchar](max) NULL,
	[Upgrade_account] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]

GO
SET ANSI_PADDING OFF
GO
/****** Object:  Table [dbo].[Token_purchase]    Script Date: 16/7/2020 10:02:07 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[Token_purchase](
	[Account_id] [varchar](max) NULL,
	[Account_name] [varchar](max) NULL,
	[Purchase_id] [varchar](max) NULL,
	[Tokens_staked] [varchar](max) NULL,
	[Initial_stake_date] [datetime] NULL,
	[Duration_of_stake] [varchar](max) NULL,
	[Ending_stake_date] [datetime] NULL,
	[Total_interest_per_month] [varchar](max) NULL,
	[Completed_date] [datetime] NULL,
	[Tier_level_when_stake] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]

GO
SET ANSI_PADDING OFF
GO
/****** Object:  Table [dbo].[Transaction_history2]    Script Date: 16/7/2020 10:02:07 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[Transaction_history2](
	[Walletgroup_name] [varchar](max) NULL,
	[Walletgroup_id] [varchar](max) NULL,
	[Account_id] [varchar](max) NULL,
	[Account_name] [varchar](max) NULL,
	[Tokens_contributed] [varchar](max) NULL,
	[Transaction_datetime] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]

GO
SET ANSI_PADDING OFF
GO
/****** Object:  Table [dbo].[Wallet_group]    Script Date: 16/7/2020 10:02:07 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[Wallet_group](
	[Account_id] [varchar](max) NULL,
	[Account_name] [varchar](max) NULL,
	[Walletgroup_name] [varchar](max) NULL,
	[Walletgroup_id] [varchar](max) NULL,
	[Goals] [varchar](max) NULL,
	[Collaborators] [varchar](max) NULL,
	[Description] [varchar](max) NULL,
	[Tokens_contributed] [varchar](max) NULL,
	[Chat_date] [varchar](max) NULL,
	[Chat_text] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]

GO
SET ANSI_PADDING OFF
GO
INSERT [dbo].[Account_information2] ([Account_id], [Account_name], [Password], [Email], [Account_balance], [Walletgroup_name], [Walletgroup_id], [Saver_points], [Tier_level], [Saver_points_spent], [Upgrade_account]) VALUES (N'A52521', N'joel', N'joel', N'joel', N'882', N'Joels group,hi,yay,yayy', N'w90830,w42433,w75134,w42670', N'0', N'Bronze', N'0', N'No')
INSERT [dbo].[Account_information2] ([Account_id], [Account_name], [Password], [Email], [Account_balance], [Walletgroup_name], [Walletgroup_id], [Saver_points], [Tier_level], [Saver_points_spent], [Upgrade_account]) VALUES (N'A27091', N'Zephan Chin', N'zephan', N'zephan', N'908', N'zephan group', N'w89288', N'0', N'Bronze', N'0', N'No')
INSERT [dbo].[Account_information2] ([Account_id], [Account_name], [Password], [Email], [Account_balance], [Walletgroup_name], [Walletgroup_id], [Saver_points], [Tier_level], [Saver_points_spent], [Upgrade_account]) VALUES (N'A96696', N'Ignatius Wong', N'iggy', N'iggy', N'820', N'iggy group', N'w84407', N'0', N'Bronze', N'0', N'No')
INSERT [dbo].[Account_information2] ([Account_id], [Account_name], [Password], [Email], [Account_balance], [Walletgroup_name], [Walletgroup_id], [Saver_points], [Tier_level], [Saver_points_spent], [Upgrade_account]) VALUES (N'A19482', N'Mr. Peter', N'peter', N'peter', N'0', N'peter group', N'w99622', N'0', N'Bronze', N'0', N'No')
INSERT [dbo].[Account_information2] ([Account_id], [Account_name], [Password], [Email], [Account_balance], [Walletgroup_name], [Walletgroup_id], [Saver_points], [Tier_level], [Saver_points_spent], [Upgrade_account]) VALUES (N'A59452', N'koo kar wai', N'kw', N'kw', N'4529', N'university fee,Kar Wai Birthday,Skateboard,Graduation Trip,For Entertainment,hello', N'w17835,w45974,w24011,w51680,w35428,w57896', N'7500.0', N'Black', N'1500.0', N'Upgrade')
INSERT [dbo].[Token_purchase] ([Account_id], [Account_name], [Purchase_id], [Tokens_staked], [Initial_stake_date], [Duration_of_stake], [Ending_stake_date], [Total_interest_per_month], [Completed_date], [Tier_level_when_stake]) VALUES (N'A10831', N'koo kar wai', N'P29547', N'1000', CAST(N'2020-07-12 16:27:18.260' AS DateTime), N'100', CAST(N'2020-10-20 16:27:18.260' AS DateTime), N'0.105', NULL, N'Bronze')
INSERT [dbo].[Token_purchase] ([Account_id], [Account_name], [Purchase_id], [Tokens_staked], [Initial_stake_date], [Duration_of_stake], [Ending_stake_date], [Total_interest_per_month], [Completed_date], [Tier_level_when_stake]) VALUES (N'A59452', N'koo kar wai', N'P26542', N'5', CAST(N'2020-07-12 17:17:31.840' AS DateTime), N'3', CAST(N'2020-07-15 17:17:31.840' AS DateTime), N'0.003', NULL, N'Bronze')
INSERT [dbo].[Token_purchase] ([Account_id], [Account_name], [Purchase_id], [Tokens_staked], [Initial_stake_date], [Duration_of_stake], [Ending_stake_date], [Total_interest_per_month], [Completed_date], [Tier_level_when_stake]) VALUES (N'A59452', N'koo kar wai', N'P54509', N'2300', CAST(N'2020-07-12 17:18:01.840' AS DateTime), N'360', CAST(N'2021-07-07 17:18:01.840' AS DateTime), N'0.375', NULL, N'Bronze')
INSERT [dbo].[Token_purchase] ([Account_id], [Account_name], [Purchase_id], [Tokens_staked], [Initial_stake_date], [Duration_of_stake], [Ending_stake_date], [Total_interest_per_month], [Completed_date], [Tier_level_when_stake]) VALUES (N'A59452', N'koo kar wai', N'P56953', N'76', CAST(N'2020-07-12 17:18:26.110' AS DateTime), N'24', CAST(N'2020-08-05 17:18:26.110' AS DateTime), N'0.034', NULL, N'Bronze')
INSERT [dbo].[Token_purchase] ([Account_id], [Account_name], [Purchase_id], [Tokens_staked], [Initial_stake_date], [Duration_of_stake], [Ending_stake_date], [Total_interest_per_month], [Completed_date], [Tier_level_when_stake]) VALUES (N'A59452', N'koo kar wai', N'P47065', N'100', CAST(N'2020-07-12 17:18:38.767' AS DateTime), N'100', CAST(N'2020-10-20 17:18:38.767' AS DateTime), N'0.105', NULL, N'Bronze')
INSERT [dbo].[Token_purchase] ([Account_id], [Account_name], [Purchase_id], [Tokens_staked], [Initial_stake_date], [Duration_of_stake], [Ending_stake_date], [Total_interest_per_month], [Completed_date], [Tier_level_when_stake]) VALUES (N'A59452', N'koo kar wai', N'P71207', N'24', CAST(N'2020-07-12 17:18:52.257' AS DateTime), N'46', CAST(N'2020-08-27 17:18:52.257' AS DateTime), N'0.066', NULL, N'Bronze')
INSERT [dbo].[Token_purchase] ([Account_id], [Account_name], [Purchase_id], [Tokens_staked], [Initial_stake_date], [Duration_of_stake], [Ending_stake_date], [Total_interest_per_month], [Completed_date], [Tier_level_when_stake]) VALUES (N'A59452', N'koo kar wai', N'P99672', N'2400', CAST(N'2020-07-12 17:26:31.393' AS DateTime), N'365', CAST(N'2021-07-12 17:26:31.393' AS DateTime), N'0.38', NULL, N'Bronze')
INSERT [dbo].[Token_purchase] ([Account_id], [Account_name], [Purchase_id], [Tokens_staked], [Initial_stake_date], [Duration_of_stake], [Ending_stake_date], [Total_interest_per_month], [Completed_date], [Tier_level_when_stake]) VALUES (N'A52521', N'joel', N'P11626', N'1000', CAST(N'2020-07-12 17:27:54.070' AS DateTime), N'50', CAST(N'2020-08-31 17:27:54.070' AS DateTime), N'0.075', NULL, N'Bronze')
INSERT [dbo].[Token_purchase] ([Account_id], [Account_name], [Purchase_id], [Tokens_staked], [Initial_stake_date], [Duration_of_stake], [Ending_stake_date], [Total_interest_per_month], [Completed_date], [Tier_level_when_stake]) VALUES (N'A27091', N'Zephan Chin', N'P13207', N'1000', CAST(N'2020-07-12 17:28:33.773' AS DateTime), N'50', CAST(N'2020-08-31 17:28:33.773' AS DateTime), N'0.075', NULL, N'Bronze')
INSERT [dbo].[Token_purchase] ([Account_id], [Account_name], [Purchase_id], [Tokens_staked], [Initial_stake_date], [Duration_of_stake], [Ending_stake_date], [Total_interest_per_month], [Completed_date], [Tier_level_when_stake]) VALUES (N'A96696', N'Ignatius Wong', N'P93139', N'1000', CAST(N'2020-07-12 17:29:23.620' AS DateTime), N'50', CAST(N'2020-08-31 17:29:23.620' AS DateTime), N'0.075', NULL, N'Bronze')
INSERT [dbo].[Token_purchase] ([Account_id], [Account_name], [Purchase_id], [Tokens_staked], [Initial_stake_date], [Duration_of_stake], [Ending_stake_date], [Total_interest_per_month], [Completed_date], [Tier_level_when_stake]) VALUES (N'A52521', N'joel', N'P41371', N'30', CAST(N'2020-07-13 16:12:16.563' AS DateTime), N'30', CAST(N'2020-08-12 16:12:16.563' AS DateTime), N'0.045', NULL, N'Bronze')
INSERT [dbo].[Token_purchase] ([Account_id], [Account_name], [Purchase_id], [Tokens_staked], [Initial_stake_date], [Duration_of_stake], [Ending_stake_date], [Total_interest_per_month], [Completed_date], [Tier_level_when_stake]) VALUES (N'A52521', N'joel', N'P80741', N'100', CAST(N'2020-07-13 17:38:00.467' AS DateTime), N'50', CAST(N'2020-09-01 17:38:00.467' AS DateTime), N'0.075', NULL, N'Bronze')
INSERT [dbo].[Token_purchase] ([Account_id], [Account_name], [Purchase_id], [Tokens_staked], [Initial_stake_date], [Duration_of_stake], [Ending_stake_date], [Total_interest_per_month], [Completed_date], [Tier_level_when_stake]) VALUES (N'A59452', N'koo kar wai', N'P27181', N'30', CAST(N'2020-07-13 17:40:06.910' AS DateTime), N'1', CAST(N'2020-07-14 17:40:06.910' AS DateTime), N'0.001', NULL, N'Bronze')
INSERT [dbo].[Token_purchase] ([Account_id], [Account_name], [Purchase_id], [Tokens_staked], [Initial_stake_date], [Duration_of_stake], [Ending_stake_date], [Total_interest_per_month], [Completed_date], [Tier_level_when_stake]) VALUES (N'A52521', N'joel', N'P64045', N'200', CAST(N'2020-07-14 18:41:06.760' AS DateTime), N'50', CAST(N'2020-09-02 18:41:06.760' AS DateTime), N'0.075', NULL, N'Bronze')
INSERT [dbo].[Token_purchase] ([Account_id], [Account_name], [Purchase_id], [Tokens_staked], [Initial_stake_date], [Duration_of_stake], [Ending_stake_date], [Total_interest_per_month], [Completed_date], [Tier_level_when_stake]) VALUES (N'A59452', N'koo kar wai', N'P17131', N'50', CAST(N'2020-07-15 11:14:30.897' AS DateTime), N'10', CAST(N'2020-07-25 11:14:30.897' AS DateTime), N'0.765', NULL, N'Black')
INSERT [dbo].[Token_purchase] ([Account_id], [Account_name], [Purchase_id], [Tokens_staked], [Initial_stake_date], [Duration_of_stake], [Ending_stake_date], [Total_interest_per_month], [Completed_date], [Tier_level_when_stake]) VALUES (N'A59452', N'koo kar wai', N'P71873', N'10', CAST(N'2020-07-14 18:51:19.137' AS DateTime), N'2', CAST(N'2020-07-16 18:51:19.137' AS DateTime), N'0.002', NULL, N'Bronze')
INSERT [dbo].[Token_purchase] ([Account_id], [Account_name], [Purchase_id], [Tokens_staked], [Initial_stake_date], [Duration_of_stake], [Ending_stake_date], [Total_interest_per_month], [Completed_date], [Tier_level_when_stake]) VALUES (N'A59452', N'koo kar wai', N'P98552', N'100', CAST(N'2020-07-14 21:13:03.197' AS DateTime), N'50', CAST(N'2020-09-02 21:13:03.197' AS DateTime), N'0.075', NULL, N'Bronze')
INSERT [dbo].[Transaction_history2] ([Walletgroup_name], [Walletgroup_id], [Account_id], [Account_name], [Tokens_contributed], [Transaction_datetime]) VALUES (N'karwai', N'w19869', N'A10831', N'koo kar wai', N'50', N'Jul 12 2020  4:52PM')
INSERT [dbo].[Transaction_history2] ([Walletgroup_name], [Walletgroup_id], [Account_id], [Account_name], [Tokens_contributed], [Transaction_datetime]) VALUES (N'For Entertainment', N'w35428', N'A59452', N'koo kar wai', N'112', N'Jul 12 2020  5:21PM')
INSERT [dbo].[Transaction_history2] ([Walletgroup_name], [Walletgroup_id], [Account_id], [Account_name], [Tokens_contributed], [Transaction_datetime]) VALUES (N'Skateboard', N'w24011', N'A59452', N'koo kar wai', N'45', N'Jul 12 2020  5:22PM')
INSERT [dbo].[Transaction_history2] ([Walletgroup_name], [Walletgroup_id], [Account_id], [Account_name], [Tokens_contributed], [Transaction_datetime]) VALUES (N'Kar Wai Birthday', N'w45974', N'A59452', N'koo kar wai', N'100', N'Jul 12 2020  5:23PM')
INSERT [dbo].[Transaction_history2] ([Walletgroup_name], [Walletgroup_id], [Account_id], [Account_name], [Tokens_contributed], [Transaction_datetime]) VALUES (N'Graduation Trip', N'w51680', N'A59452', N'koo kar wai', N'294', N'Jul 12 2020  5:25PM')
INSERT [dbo].[Transaction_history2] ([Walletgroup_name], [Walletgroup_id], [Account_id], [Account_name], [Tokens_contributed], [Transaction_datetime]) VALUES (N'Graduation Trip', N'w51680', N'A52521', N'joel', N'134', N'Jul 12 2020  5:30PM')
INSERT [dbo].[Transaction_history2] ([Walletgroup_name], [Walletgroup_id], [Account_id], [Account_name], [Tokens_contributed], [Transaction_datetime]) VALUES (N'Graduation Trip', N'w51680', N'A96696', N'Ignatius Wong', N'76', N'Jul 12 2020  5:30PM')
INSERT [dbo].[Transaction_history2] ([Walletgroup_name], [Walletgroup_id], [Account_id], [Account_name], [Tokens_contributed], [Transaction_datetime]) VALUES (N'Graduation Trip', N'w51680', N'A96696', N'Ignatius Wong', N'19', N'Jul 12 2020  5:31PM')
INSERT [dbo].[Transaction_history2] ([Walletgroup_name], [Walletgroup_id], [Account_id], [Account_name], [Tokens_contributed], [Transaction_datetime]) VALUES (N'Graduation Trip', N'w51680', N'A52521', N'joel', N'200', N'Jul 12 2020  5:32PM')
INSERT [dbo].[Transaction_history2] ([Walletgroup_name], [Walletgroup_id], [Account_id], [Account_name], [Tokens_contributed], [Transaction_datetime]) VALUES (N'Graduation Trip', N'w51680', N'A27091', N'Zephan Chin', N'32', N'Jul 12 2020  5:33PM')
INSERT [dbo].[Transaction_history2] ([Walletgroup_name], [Walletgroup_id], [Account_id], [Account_name], [Tokens_contributed], [Transaction_datetime]) VALUES (N'Graduation Trip', N'w51680', N'A96696', N'Ignatius Wong', N'85', N'Jul 12 2020  5:34PM')
INSERT [dbo].[Transaction_history2] ([Walletgroup_name], [Walletgroup_id], [Account_id], [Account_name], [Tokens_contributed], [Transaction_datetime]) VALUES (N'Graduation Trip', N'w51680', N'A52521', N'joel', N'100', N'Jul 12 2020  5:35PM')
INSERT [dbo].[Transaction_history2] ([Walletgroup_name], [Walletgroup_id], [Account_id], [Account_name], [Tokens_contributed], [Transaction_datetime]) VALUES (N'Graduation Trip', N'w51680', N'A27091', N'Zephan Chin', N'60', N'Jul 12 2020  5:36PM')
INSERT [dbo].[Transaction_history2] ([Walletgroup_name], [Walletgroup_id], [Account_id], [Account_name], [Tokens_contributed], [Transaction_datetime]) VALUES (N'University Fees', N'w17835', N'A52521', N'joel', N'3', N'Jul 13 2020  4:09PM')
INSERT [dbo].[Transaction_history2] ([Walletgroup_name], [Walletgroup_id], [Account_id], [Account_name], [Tokens_contributed], [Transaction_datetime]) VALUES (N'Kar Wai Birthday', N'w45974', N'A52521', N'joel', N'1', N'Jul 13 2020  5:31PM')
INSERT [dbo].[Transaction_history2] ([Walletgroup_name], [Walletgroup_id], [Account_id], [Account_name], [Tokens_contributed], [Transaction_datetime]) VALUES (N'Joel group', N'w90830', N'A52521', N'joel', N'10', N'Jul 14 2020  6:31PM')
INSERT [dbo].[Transaction_history2] ([Walletgroup_name], [Walletgroup_id], [Account_id], [Account_name], [Tokens_contributed], [Transaction_datetime]) VALUES (N'University Fees', N'w17835', N'A59452', N'koo kar wai', N'1', N'Jul 15 2020 10:19AM')
INSERT [dbo].[Transaction_history2] ([Walletgroup_name], [Walletgroup_id], [Account_id], [Account_name], [Tokens_contributed], [Transaction_datetime]) VALUES (N'University Fees', N'w17835', N'A59452', N'koo kar wai', N'10', N'Jul 15 2020 10:50AM')
INSERT [dbo].[Transaction_history2] ([Walletgroup_name], [Walletgroup_id], [Account_id], [Account_name], [Tokens_contributed], [Transaction_datetime]) VALUES (N'University Fees', N'w17835', N'A59452', N'koo kar wai', N'3', N'Jul 14 2020  9:05PM')
INSERT [dbo].[Transaction_history2] ([Walletgroup_name], [Walletgroup_id], [Account_id], [Account_name], [Tokens_contributed], [Transaction_datetime]) VALUES (N'University Fees', N'w17835', N'A59452', N'koo kar wai', N'1', N'Jul 15 2020 10:37AM')
INSERT [dbo].[Wallet_group] ([Account_id], [Account_name], [Walletgroup_name], [Walletgroup_id], [Goals], [Collaborators], [Description], [Tokens_contributed], [Chat_date], [Chat_text]) VALUES (N'A59452', N'koo kar wai', N'university fee', N'w17835', N'6000', N'joel,Zephan Chin,Ignatius Wong,Mr. Peter', N'hello', N'18', N'[Sent at 2020-07-13 16:10:06.240000],[Sent at 2020-07-13 16:10:12.040000],[Sent at 2020-07-14 21:07:12.833000],[Sent at 2020-07-14 21:15:42.987000],[Sent at 2020-07-15 10:52:11.850000]', N'joel: hi,joel: yay,koo kar wai: hi,joel: exit,koo kar wai: hi')
INSERT [dbo].[Wallet_group] ([Account_id], [Account_name], [Walletgroup_name], [Walletgroup_id], [Goals], [Collaborators], [Description], [Tokens_contributed], [Chat_date], [Chat_text]) VALUES (N'A59452', N'koo kar wai', N'Kar Wai Birthday', N'w45974', N'500', N'Zephan Chin,joel,Ignatius Wong,Mr. Peter', N'happy birthday', N'101', N'[Sent at 2020-07-13 17:31:47.520000]', N'joel: Hello')
INSERT [dbo].[Wallet_group] ([Account_id], [Account_name], [Walletgroup_name], [Walletgroup_id], [Goals], [Collaborators], [Description], [Tokens_contributed], [Chat_date], [Chat_text]) VALUES (N'A59452', N'koo kar wai', N'Skateboard', N'w24011', N'80', N'NULL', N'try skateboarding as a new hobby', N'45', N'NULL', N'NULL')
INSERT [dbo].[Wallet_group] ([Account_id], [Account_name], [Walletgroup_name], [Walletgroup_id], [Goals], [Collaborators], [Description], [Tokens_contributed], [Chat_date], [Chat_text]) VALUES (N'A59452', N'koo kar wai', N'Graduation Trip', N'w51680', N'3000', N'joel,Zephan Chin,Ignatius Wong', N'Lets save up to go Tokyo together', N'1000', N'NULL', N'NULL')
INSERT [dbo].[Wallet_group] ([Account_id], [Account_name], [Walletgroup_name], [Walletgroup_id], [Goals], [Collaborators], [Description], [Tokens_contributed], [Chat_date], [Chat_text]) VALUES (N'A59452', N'koo kar wai', N'For Entertainment', N'w35428', N'150', N'NULL', N'buy a few more games for my PS4', N'112', N'NULL', N'NULL')
INSERT [dbo].[Wallet_group] ([Account_id], [Account_name], [Walletgroup_name], [Walletgroup_id], [Goals], [Collaborators], [Description], [Tokens_contributed], [Chat_date], [Chat_text]) VALUES (N'A52521', N'joel', N'Joels group', N'w90830', N'2000', N'Zephan Chin,koo kar wai', N'joels group', N'10', N'[Sent at 2020-07-14 18:33:26.380000]', N'joel: Hello')
INSERT [dbo].[Wallet_group] ([Account_id], [Account_name], [Walletgroup_name], [Walletgroup_id], [Goals], [Collaborators], [Description], [Tokens_contributed], [Chat_date], [Chat_text]) VALUES (N'A27091', N'Zephan Chin', N'zephan group', N'w89288', N'1000', N'NULL', N'zephan group', N'0', N'NULL', N'NULL')
INSERT [dbo].[Wallet_group] ([Account_id], [Account_name], [Walletgroup_name], [Walletgroup_id], [Goals], [Collaborators], [Description], [Tokens_contributed], [Chat_date], [Chat_text]) VALUES (N'A96696', N'Ignatius Wong', N'iggy group', N'w84407', N'1000', N'NULL', N'iggy group', N'0', N'NULL', N'NULL')
INSERT [dbo].[Wallet_group] ([Account_id], [Account_name], [Walletgroup_name], [Walletgroup_id], [Goals], [Collaborators], [Description], [Tokens_contributed], [Chat_date], [Chat_text]) VALUES (N'A19482', N'Mr. Peter', N'peter group', N'w99622', N'1000', N'NULL', N'peter group', N'0', N'NULL', N'NULL')
INSERT [dbo].[Wallet_group] ([Account_id], [Account_name], [Walletgroup_name], [Walletgroup_id], [Goals], [Collaborators], [Description], [Tokens_contributed], [Chat_date], [Chat_text]) VALUES (N'A52521', N'joel', N'hi', N'w42433', N'3000', N'NULL', N'yo', N'0', N'NULL', N'NULL')
INSERT [dbo].[Wallet_group] ([Account_id], [Account_name], [Walletgroup_name], [Walletgroup_id], [Goals], [Collaborators], [Description], [Tokens_contributed], [Chat_date], [Chat_text]) VALUES (N'A52521', N'joel', N'yay', N'w75134', N'3000', N'NULL', N'yay', N'0', N'NULL', N'NULL')
INSERT [dbo].[Wallet_group] ([Account_id], [Account_name], [Walletgroup_name], [Walletgroup_id], [Goals], [Collaborators], [Description], [Tokens_contributed], [Chat_date], [Chat_text]) VALUES (N'A52521', N'joel', N'yayy', N'w42670', N'3000', N'NULL', N'yay', N'0', N'NULL', N'NULL')
INSERT [dbo].[Wallet_group] ([Account_id], [Account_name], [Walletgroup_name], [Walletgroup_id], [Goals], [Collaborators], [Description], [Tokens_contributed], [Chat_date], [Chat_text]) VALUES (N'A59452', N'koo kar wai', N'hello', N'w57896', N'10000', N'NULL', N'yay', N'0', N'NULL', N'NULL')
USE [master]
GO
ALTER DATABASE [Definite CA2] SET  READ_WRITE 
GO
